__author__ = "Matt Zheng"


import re

# tone diacritic → base+digit
tone_symbols = {
    'á': ('a', '2'), 'à': ('a', '3'), 'â': ('a', '5'), 'ā': ('a', '7'),
    'a̍': ('a', '8'), 'a̋': ('a', '9'),
    'é': ('e', '2'), 'è': ('e', '3'), 'ê': ('e', '5'), 'ē': ('e', '7'),
    'e̍': ('e', '8'),
    'í': ('i', '2'), 'ì': ('i', '3'), 'î': ('i', '5'), 'ī': ('i', '7'),
    'i̍': ('i', '8'),
    'ó': ('o', '2'), 'ò': ('o', '3'), 'ô': ('o', '5'), 'ō': ('o', '7'),
    'o̍͘': ('o', '8'),
    'ú': ('u', '2'), 'ù': ('u', '3'), 'û': ('u', '5'), 'ū': ('u', '7'),
    'u̍': ('u', '8'),
}

# consonant mapping
# Neurlang: removed tie bar (t͡, d͡). We don't currently use tie bar in other languages or any languages or support it.
consonant_map = {
    'ph': 'pʰ',
    'tsh': 'tsʰ',
    'ch': 'ts',
    'ng': 'ŋ',
    'kh': 'kʰ',
    'th': 'tʰ',
    'j': 'dz',
    'b': 'b',
    'p': 'p',
    'm': 'm',
    't': 't',
    'n': 'n',
    'l': 'l',
    'k': 'k',
    'g': 'g',
    's': 's',
    'h': 'h',
    'ts': 'ts'
}

# vowel mapping
# > common vowel 
# 1-1 口音韻
# 1-2 鼻音韻
# 2 陽聲韻
# 3-1 普通喉塞韻
# 3-2 鼻化喉塞韻
# 3-3 普通入聲韻
# > special vowel, not commonly use
# (a) 陰聲韻
# (b) 陽聲韻
# (c) 入聲韻
vowel_map = {
    'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u',
    'oo': 'ɔ', 'ai': 'ai', 'au': 'au', 'ia': 'ia',
    'io': 'io', 'iu': 'iu', 'ua': 'ua', 'ue': 'ue',
    'ui': 'ui', 'iau': 'iau', 'uai': 'uai',
    
    'ann': 'ã', 'enn': 'ẽ', 'inn': 'ĩ', 'onn': 'õ', 'm': 'm',
    'ng': 'ŋ', 'iaunn': 'ĩãũ', 'uainn': 'ũãĩ',
    'uann': 'ũã', 'iann': 'ĩã', 'iunn': 'ĩũ', 'ainn': 'ãĩ',

    'am': 'am', 'an': 'an', 'ang': 'aŋ', 'im': 'im', 'in': 'in',
    'ing': 'iŋ', 'om': 'om', 'ong': 'oŋ', 'iam': 'iam', 'ian': 'ian',
    'iang': 'iaŋ', 'iong': 'ioŋ', 'un': 'un', 'uan': 'uan',

    'ah': 'aʔ', 'eh': 'eʔ', 'ih': 'iʔ', 'oh': 'oʔ', 'uh': 'uʔ',
    'iah': 'iaʔ', 'auh': 'auʔ', 'ioh': 'ioʔ', 'iuh': 'iuʔ',
    'iauh': 'iauʔ', 'uah': 'uaʔ', 'ueh': 'ueʔ', 'ooh': 'ɔʔ',

    'annh': 'ãʔ', 'ennh': 'ẽʔ', 'innh': 'ĩʔ', 'mh': 'mʔ', 'iannh': 'ĩãʔ', 'ngh': 'ŋʔ',

    'ap': 'ap', 'at': 'at', 'ak': 'ak', 'op': 'op', 'ok': 'ok',
    'iok': 'iok', 'ip': 'ip', 'it': 'it', 'ik': 'ik', 'iap': 'iap',
    'iat': 'iat', 'iak': 'iak', 'ut': 'ut', 'uat': 'uat',

    'ioo': 'iɔ', 'ir': 'ɨ', 'ere': 'ɘe', 'er': 'ɘ',
    'irinn': 'ɨĩ', 'ee': 'ɛ', 'uee': 'uɛ', 'eeh': 'ɛh',
    'uinn': 'ũĩ', 'ionn': 'ĩɔ̃',

    'irm': 'ɨm', 'irn': 'ɨn', 'irng': 'ɨŋ', 'eng': 'ɛŋ', 'uang': 'uaŋ',

    'aih': 'aih', 'ainnh': 'ãĩʔ', 'aunnh': 'ãũʔ', 'erh': 'ɘʔ',
    'ereh': 'ɘeʔ', 'uih': 'uiʔ', 'irp': 'ɨp', 'irt': 'ɨt', 'irk': 'ɨk'
}

# tone mapping
tone_map = {
    '1': '˥˥', '2': '˥˧', '3': '˨˩',
    '4': '˨', '5': '˨˦', '6': '˨˨',
    '7': '˧˧', '8': '˦', '9': '˧˥'
}


def tai_lo_symbol_to_number(syllable, category):
    """Convert a single Tâi-lô syllable with tone marks → tone‐number form."""
    if not syllable:
        return syllable

    syl = syllable
    tone_applied = False

    # 2) Look for any tone symbol, replace it, append the digit
    for sym, (base, digit) in tone_symbols.items():
        if sym in syl:
            syl = syl.replace(sym, base)
            syl += digit
            tone_applied = True
            break

    # 3) Strip any leftover combining marks (Mn = Nonspacing Mark)
    syl = ''.join(ch for ch in syl if category(ch) != 'Mn')

    # 4) If no tone yet, infer: checked finals → 4, else → 1
    if not tone_applied:
        # pull off any trailing digits first
        m = re.match(r'^(.*?)(\d?)$', syl)
        base = m.group(1)
        if base and base[-1] in ('p', 't', 'k', 'h'):
            syl = base + '4'
        else:
            syl = base + '1'

    return syl

def tai_lo_to_ipa(tai_lo, category):
    # remove trailing dot
    if tai_lo.endswith('.'):
        tai_lo = tai_lo[:-1]
    tai_lo = tai_lo.lower()
    ipa_words = []

    for word in tai_lo.split():
        # if a word has '/', process each alt separately
        alts = []
        for alt in word.split('/'):
            syllables = alt.split('-')
            out_syl = []

            for syl in syllables:
                numbered = tai_lo_symbol_to_number(syl, category)

                # split into base and tone
                m = re.match(r'^([a-z]+)(\d)$', numbered, re.IGNORECASE)
                if not m:
                    out_syl.append(numbered)
                    continue
                base, tone = m.groups()

                # consonant
                ipa = ''
                for L in range(3, -1, -1):
                    head = base[:L]
                    if head in consonant_map:
                        ipa += consonant_map[head]
                        rest = base[L:]
                        break
                else:
                    rest = base

                # vowel(s)
                i = 0
                while i < len(rest):
                    # try the longest match in vowel_map
                    for j in range(len(rest), i, -1):
                        piece = rest[i:j]
                        if piece in vowel_map:
                            ipa += vowel_map[piece]
                            i = j - 1
                            break
                    i += 1

                # tone
                ipa += tone_map[tone]
                out_syl.append(ipa)

            alts.append('-'.join(out_syl))
        ipa_words.append('/'.join(alts))

    return ' '.join(ipa_words)

matching_punct = [[" ", " "],[".", "。"],[")", "）"],["(", "（"],[")", ")"],["(", "("],["?", "？"],[",","，"],[";","；"],["!","！"]]

def trim_tai_lo(text):
    for punct in matching_punct:
        text = text.strip(punct[0])
    return text

def trim_characters(text):
    for punct in matching_punct:
        text = text.strip(punct[1])
    return text

def split_same(text0, text1):
    for punct in matching_punct:
        if text0.count(punct[0]) == text1.count(punct[1]):
            text0 = text0.replace(punct[0], '\t')
            text1 = text1.replace(punct[1], '\t')
    text0 = text0.split('\t')
    text1 = text1.split('\t')
    return (text0, text1)

def ipa_clean(ipa):
    return ipa.replace(" ", "").replace("-", "")

# Usage
# print(tai_lo_to_ipa("Liâm-mi beh tsò-hong-thai--lah!"))

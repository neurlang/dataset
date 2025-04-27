__author__ = "Matt Zheng"


import re

# symbol tone to tone number mapping
tone_symbols = {
    'á': 'a2', 'à': 'a3', 'â': 'a5', 'ā': 'a7', 'a̍': 'a8', 'a̋': 'a9',
    'é': 'e2', 'è': 'e3', 'ê': 'e5', 'ē': 'e7', 'e̍': 'e8',
    'í': 'i2', 'ì': 'i3', 'î': 'i5', 'ī': 'i7', 'i̍': 'i8',
    'ó': 'o2', 'ò': 'o3', 'ô': 'o5', 'ō': 'o7', 'o̍͘': 'o8',
    'ú': 'u2', 'ù': 'u3', 'û': 'u5', 'ū': 'u7', 'u̍': 'u8'
}

# consonant mapping
consonant_map = {
    'ph': 'pʰ', 'tsh': 't͡sʰ', 'ch': 't͡s', 'ng': 'ŋ',
    'kh': 'kʰ', 'th': 'tʰ', 'j': 'd͡z', 'b': 'b',
    'p': 'p', 'm': 'm', 't': 't', 'n': 'n',
    'l': 'l', 'k': 'k', 'g': 'ɡ', 's': 's',
    'h': 'h', 'ts': 'ts'
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


def tai_lo_symbol_to_number(word):
    # turn symbol tone to tone number
    if word == '': return word
    for c in word:
        if c in tone_symbols:
            word = word.replace(c, tone_symbols[c][0])
            word += tone_symbols[c][1]
            break
        elif ord(c) == 781:
            word = word.replace(c, '')
            word += '8'
            break
        elif ord(c) == 779:
            word = word.replace(c, '')
            word += '9'
            break
    if word[-1] == 'p' or word[-1] == 't' or word[-1] == 'k' or word[-1] == 'h':
        word += '4'
    if ord(word[-1]) > 96:
        word += '1'
    return word


def tai_lo_to_ipa(tai_lo):
    if tai_lo == "": return tai_lo
    # text preprocessor
    if tai_lo[-1] == '.':
        tai_lo = tai_lo[:-1]  # remove dot
    tai_lo = tai_lo.lower()  # convert input to lowercase

    ipa_result = []
    for word in tai_lo.split():
        # print('process: %s' % word)
        syllables = word.split('-')
        result = []

        for syllable in syllables:
            # convert input to tone number
            syllable = tai_lo_symbol_to_number(syllable)

            # this will split phone & tone
            # eg: guat8 -> syllable = "guat", tone = "8"
            match = re.match(r'([a-zA-Z]+)(\d?)$', syllable, re.IGNORECASE)
            if not match:
                result.append(syllable)
                continue
            
            syllable, tone = match.groups()
            ipa = ''

            # processing consonant
            for cons_index in range(3, -1, -1):
                if cons_index > len(syllable): continue
                if syllable[0:cons_index] in consonant_map:
                    ipa += consonant_map[syllable[0:cons_index]]
                    break

            # processing vowel
            left = cons_index
            for vowel_index in range(len(syllable), cons_index, -1):
                if syllable[left:vowel_index] in vowel_map:
                    ipa += vowel_map[syllable[left:vowel_index]]
                    left = vowel_index

            # processing tone
            if tone in tone_map:
                ipa += tone_map[tone]

            result.append(ipa)

        ipa_result.append('-'.join(result))

    return ' '.join(ipa_result)


# Usage
# print(tai_lo_to_ipa("Liâm-mi beh tsò-hong-thai--lah!"))
__author__ = "Matt Zheng"


import re

# symbol tone to tone number mapping
tone_symbols = {
    'á': 'a2', 'à': 'a3', 'â': 'a5', 'ā': 'a7', 'a̍': 'a8',
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
    'h': 'h'
}

# vowel mapping
vowel_map = {
    'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u',
    'oo': 'ɔ', 'ai': 'ai', 'au': 'au', 'ia': 'ia',
    'io': 'io', 'iu': 'iu', 'ua': 'ua', 'uo': 'uo',
    'ui': 'ui', 'iau': 'iau', 'uai': 'uai', 'am': 'am',
    'an': 'an', 'ang': 'aŋ', 'ap': 'ap', 'at': 'at',
    'ak': 'ak', 'ann': 'ã', 'enn': 'ẽ', 'uat': 'uat',
    'inn': 'ĩ', 'onn': 'õ', 'unn': 'ũ', 'iann': 'ĩã',
    'iunn': 'ĩũ', 'ainn': 'ãĩ'
}

# tone mapping
tone_map = {
    '1': '˥˥', '2': '˥˧', '3': '˨˩',
    '4': '˨', '5': '˨˦', '6': '˨˨',
    '7': '˧˧', '8': '˦'
}


def tai_lo_symbol_to_number(word):
    # turn symbol tone to tone number
    if word == '': return word
    for c in word:
        if c in tone_symbols:
            word = word.replace(c, tone_symbols[c][0])
            word += tone_symbols[c][1]
            break
        if ord(c) == 781:
            word = word.replace(c, '')
            word += '8'
            break
    if word[-1] == 'p' or word[-1] == 't' or word[-1] == 'k':
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
# print(tai_lo_to_ipa("phùn--tio̍h"))
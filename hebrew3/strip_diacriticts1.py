import regex as re
import unicodedata

def strip_hebrew_punctuation2(text):
    text = text.replace('|', '')
    text = text.replace('.', '')
    text = text.replace('?', '')
    text = text.replace('!', '')
    text = text.replace(',', '')
    text = text.replace('-', '')
    return text
# Hebrew diacritics are marks (category Mn)
# This regex removes all marks from each word
def strip_hebrew_punctuation(text):
    # Remove | character anywhere
    return re.sub(r'\p{M}+', '', text)

input_file = 'words_phonemes.txt'
output_file = 'lexicon.tsv'
morphs_file = 'morphs.tsv'

dictionary = {}
dictionary_stripped = {}

with open(morphs_file, 'r', encoding='utf-8') as morphsfile:
    for line in morphsfile:
        if '\t' not in line:
            continue  # skip malformed lines
        hebrew, morph = line.strip().split('\t', 1)
        hebrew = unicodedata.normalize("NFC", hebrew)
        dictionary[hebrew] = morph
        hebrew = strip_hebrew_punctuation(hebrew)
        dictionary_stripped[hebrew] = morph

with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', encoding='utf-8') as outfile:
    
    for line in infile:
        if '\t' not in line:
            continue  # skip malformed lines
        
        hebrew, ipa = line.strip().split('\t', 1)
        hebrew = unicodedata.normalize("NFC", hebrew)
        stripped_hebrew = strip_hebrew_punctuation2(hebrew)
        morph = dictionary.get(stripped_hebrew)
        stripped_hebrew = strip_hebrew_punctuation(stripped_hebrew)
        if morph is None:
            morph = dictionary_stripped.get(stripped_hebrew)
        outfile.write(f"{stripped_hebrew}\t{ipa}\t[\"{morph}\"]\n")

print(f"Done! Stripped dictionary saved to: {output_file}")

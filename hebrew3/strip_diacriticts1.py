import regex as re

# Hebrew diacritics are marks (category Mn)
# This regex removes all marks from each word
def strip_hebrew_punctuation(text):
    # Remove | character anywhere
    text = text.replace('|', '')
    return re.sub(r'\p{M}+', '', text)

input_file = 'words_phonemes.txt'
output_file = 'lexicon.tsv'

with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', encoding='utf-8') as outfile:
    
    for line in infile:
        if '\t' not in line:
            continue  # skip malformed lines
        
        hebrew, ipa = line.strip().split('\t', 1)
        stripped_hebrew = strip_hebrew_punctuation(hebrew)
        outfile.write(f"{stripped_hebrew}\t{ipa}\n")

print(f"Done! Stripped dictionary saved to: {output_file}")

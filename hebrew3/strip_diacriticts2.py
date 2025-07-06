import regex as re
from collections import Counter

# === 1. Strip Hebrew diacritics + punctuation + | ===
def strip_hebrew_word(word):
    # Remove diacritics
    word = re.sub(r'\p{M}+', '', word)
    # Remove | character anywhere
    word = word.replace('|', '')
    # Remove punctuation at edges
    word = re.sub(r'^[\.\,\?\!\:\;]+|[\.\,\?\!\:\;]+$', '', word)
    return word

# === 2. Strip IPA punctuation ===
def strip_ipa_punctuation(word):
    return re.sub(r'^[\.\,\?\!\:\;]+|[\.\,\?\!\:\;]+$', '', word)

# === 3. Load IPA word counts ===
def load_ipa_counts(lexicon_file):
    word_counts = Counter()
    with open(lexicon_file, 'r', encoding='utf-8') as f:
        for line in f:
            if '\t' not in line:
                continue
            _, ipa = line.strip().split('\t', 1)
            stripped_ipa = strip_ipa_punctuation(ipa)
            word_counts[stripped_ipa] += 1
    return word_counts

# === 4. Process sentences ===
def process_sentences(ipa_counts, sentences_file, output_file):
    with open(sentences_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        
        for line in infile:
            if '\t' not in line:
                continue

            hebrew_text, ipa_text = line.strip().split('\t', 1)
            hebrew_words = hebrew_text.strip().split()
            ipa_words = ipa_text.strip().split()

            if len(hebrew_words) != len(ipa_words):
                continue  # skip misaligned pairs

            processed_hebrew = []
            processed_ipa = []

            for hw, iw in zip(hebrew_words, ipa_words):
                stripped_hw = strip_hebrew_word(hw)
                stripped_iw = strip_ipa_punctuation(iw)

                # Mask IPA if it appears once in lexicon
                if ipa_counts.get(stripped_iw, 0) == 1:
                    processed_ipa.append('_')
                else:
                    processed_ipa.append(stripped_iw)

                processed_hebrew.append(stripped_hw)

            outfile.write(f"{' '.join(processed_hebrew)}\t{' '.join(processed_ipa)}\n")

    print(f"Processed file written to: {output_file}")

# === 5. Run ===
if __name__ == "__main__":
    lexicon_file = 'lexicon.tsv'
    sentences_file = 'knesset_phonemes_v1.txt'
    output_file = 'multi.tsv'

    ipa_counts = load_ipa_counts(lexicon_file)
    process_sentences(ipa_counts, sentences_file, output_file)

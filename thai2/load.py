from datasets import load_dataset

# Login using e.g. `huggingface-cli login` to access this dataset
ds = load_dataset("Gregniuki/g2p_thai_ipa")

matching_punct = [[" ", " "],[".", "。"],[")", "）"],["(", "（"],[")", ")"],["(", "("],["?", "？"],[",","，"],[";","；"],["!","！"]]

def trim_ipa(text):
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

for row in ds["train"]:
    text = row["ipa_transcript_word_batched_split"]
    characters = row["transcript"]
    if text is None or characters is None:
        continue
    text, characters = split_same(text, characters)
    for i in range(len(text)):
        character = trim_characters(characters[i])
        txt = trim_ipa(text[i])
        print(character + "\t" + txt.replace(' ', '').replace('.', ' ').replace('͡',''))

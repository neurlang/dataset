# generates the hokkien2 lexicon.tsv file
# the lexicon is then passed trough sort and uniq
from datasets import load_dataset
import unicodedata
import importlib  
hokkien_to_ipa = importlib.import_module("hokkien-to-ipa")

ds = load_dataset("sarahwei/Taiwanese-Minnan-Sutiau")

for row in ds['train']:
    if row['hanzi'] != row['minnan roman']:
        text = hokkien_to_ipa.trim_tai_lo(unicodedata.normalize('NFC', row['minnan roman']))
        characters = hokkien_to_ipa.trim_characters(row['hanzi'])
        text, characters = hokkien_to_ipa.split_same(text, characters)
        for i in range(len(text)):
            character = hokkien_to_ipa.trim_characters(characters[i])
            txt = hokkien_to_ipa.trim_tai_lo(text[i])
            for j in range(txt.count('/')):
                character = hokkien_to_ipa.trim_characters(characters[i])
                txt = hokkien_to_ipa.trim_tai_lo(text[i].split('/')[j])
                print(character + "\t" + hokkien_to_ipa.ipa_clean(hokkien_to_ipa.tai_lo_to_ipa(txt, unicodedata.category)) ) #+ "\t" + txt)
            else:
                print(character + "\t" + hokkien_to_ipa.ipa_clean(hokkien_to_ipa.tai_lo_to_ipa(txt, unicodedata.category)) ) # + "\t" + txt)

# The entire dataset is available for use
dataset = load_dataset("sarahwei/Taiwanese-Minnan-Example-Sentences")

for row in dataset['train']:
    if row['hanzi'] != row['minnan roman']:
        text = hokkien_to_ipa.trim_tai_lo(unicodedata.normalize('NFC', row['minnan roman']))
        characters = hokkien_to_ipa.trim_characters(row['hanzi'])
        text, characters = hokkien_to_ipa.split_same(text, characters)
        for i in range(len(text)):
            character = hokkien_to_ipa.trim_characters(characters[i])
            txt = hokkien_to_ipa.trim_tai_lo(text[i])
            for j in range(txt.count('/')):
                character = hokkien_to_ipa.trim_characters(characters[i])
                txt = hokkien_to_ipa.trim_tai_lo(text[i].split('/')[j])
                print(character + "\t" + hokkien_to_ipa.ipa_clean(hokkien_to_ipa.tai_lo_to_ipa(txt, unicodedata.category)) ) #+ "\t" + txt)
            else:
                print(character + "\t" + hokkien_to_ipa.ipa_clean(hokkien_to_ipa.tai_lo_to_ipa(txt, unicodedata.category)) ) # + "\t" + txt)

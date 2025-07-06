# README HEBREW3

## Homographs big file:

https://huggingface.co/datasets/thewh1teagle/phonikud-phonemes-data/blob/main/knesset_phonemes_v1.txt.7z

## Preprocessing

- **strip_diacriticts1.py** - already ran, generates lexicon.tsv, don't forget to remove the `|` character
- **strip_diacriticts2.py** - run after unpacking big file above, then do train/eval split

## Study tokenizer grammar

```
./study_language_reverse.sh hebrew3 --rowlossimportance 2
./study_language.sh hebrew3 --rowlossimportance 6
```

## Train/Eval split

```
python3 -m venv venv
venv/bin/pip3 install regex
venv/bin/python3 strip_diacriticts2.py
head -n 1000000 multi.tsv > multi_eval.tsv
tail -n 4329211 multi.tsv > multi_train.tsv
rm multi.tsv
mv multi_train.tsv multi.tsv
```


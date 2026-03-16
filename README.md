# IPA Phonetic dataset lexicon

## Overview

This repository provides multilingual phonetic lexicons mapping words to their **IPA (International Phonetic Alphabet) pronunciations**.

The dataset currently covers **140+ languages** and is organized as simple TSV lexicons containing word–IPA pairs. Each language directory contains a `lexicon.tsv` file with the following format:

```
word<TAB>ipa
```

Example:
```tsv
hello    həˈloʊ
world    wɝːld
```
## Dataset Structure

Each language has its own directory:

```
<language>/lexicon.tsv
<language>/<language>/lexicon.tsv
```

The files contain tab-separated pairs:

```
word    ipa_pronunciation
```

This simple structure makes the dataset easy to use in training pipelines, phonemizers, and speech systems.

## Applications

This dataset is primarily intended for:

* Grapheme-to-Phoneme (G2P) training
* Phonemization pipelines
* Text-to-Speech (TTS) systems
* Speech recognition lexicons
* Linguistic and phonetic research

It is currently used by the **goruut phonemizer**, a multilingual grapheme-to-phoneme system.

## Motivation

Recent research shows that using phonemes instead of raw text can significantly improve speech models. As discussed in the Hugging Face article *"G2P Shrinks Speech Models"*, phoneme-based pipelines can:

* reduce TTS model size
* improve pronunciation accuracy
* simplify multilingual speech modeling

This repository aims to provide a large, simple, and practical collection of IPA lexicons that can be used to build high-quality phonemization and speech systems.

# Languages not using spaces

**(thus their dataset must contain sentences too)**:

* Cantonese
* Minnan/Hokkien
* Minnan/Taiwanese
* Minnan/Hokkien2
* Minnan/Taiwanese2
* Chinese/Mandarin
* Japanese
* Tibetan
* Shantaiyai

# Licensing information:

* **MIT** Original data for the 15 languages taken from [gruut databases](https://github.com/rhasspy/gruut)
* **MIT** To this the data for the 31 languages were added [ipa dict files](https://github.com/open-dict-data/ipa-dict/)
* **CC0: Public Domain** Chinese/Mandarin-IPA language sentence pairs were generated:
  - from the chinese sentences taken from dataset [from kaggle](https://www.kaggle.com/datasets/concyclics/machine-translation-chinese-and-english)
  - based on the above dictionary and MISTRAL-nemo made IPA dictionary which was paired with chinese sentences to ipa sentences using string substitution.
* **Mozilla Public License 2.0** Chinese/Mandarin Extra missing phrases added-on from Mozilla Common Voice 19.
* **Apache-2.0** Wikipron data were added for selected large languages [from wikipron data](https://github.com/CUNY-CL/wikipron/tree/master/data/scrape/tsv)
* **cc-by-nc-4.0** Tibetan taken from [billingsmoore](https://huggingface.co/datasets/billingsmoore/tibetan-phonetic-transliteration-dataset)
* **cc-by-nc-4.0** Tibetan added more data at [billingsmoore](https://huggingface.co/datasets/billingsmoore/tibetan-to-english-translation-dataset)
* **MIT/Apache2** Slovak language is mostly self made, I hereby dedicate it under MIT/Apache2
* **CC-BY-SA 3.0**: Text in Japanese corpus is licensed as follows. The text data were modified and pronunciation information is added. basic5000 is as follows:
  - wikipedia [wikipedia](https://ja.wikipedia.org/) CC-BY-SA 3.0
  - TANAKA corpus [Tanaka_Corpus](http://www.edrdg.org/wiki/index.php/Tanaka_Corpus) CC-BY 2.0
  - JSUT (Japanese speech corpus of Saruwatari-lab., University of Tokyo) [JSUT](https://sites.google.com/site/shinnosuketakamichi/publication/jsut). CC-BY-SA 4.0
* **Mozilla Public License 2.0** Japanese City Names added-on from Mozilla Common Voice 19.
* **Apache-2.0** US/UK English data sourced from [Kokoro Misaki](https://github.com/hexgrad/misaki)
* **Unknown license** Cantonese [words](https://github.com/CanCLID/words) and [sentences](https://github.com/CanCLID/sentences) soruced from the [github](https://github.com/CanCLID)
* **Apache-2.0 license** English - Homographs data (multi.tsv) sourced mainly from: [Homograph disambiguation data](https://github.com/google-research-datasets/WikipediaHomographData)
* **cc-by-nc-sa-4.0** Hokkien Taiwanese Minnan - Data from [sarahwei](https://huggingface.co/datasets/sarahwei/Taiwanese-Minnan-Example-Sentences)
* **cc** Hebrew3 data from [thewh1teagle](https://huggingface.co/datasets/thewh1teagle/phonikud-phonemes-data)

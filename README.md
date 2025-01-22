# dataset

# languages not using spaces (thus the dataset must contain sentences too):

* Chinese
* Japanese
* Tibetan

# Licensing information:

* [MIT] Original data for the 15 languages taken from [https://github.com/rhasspy/gruut](gruut databases)
* [MIT] To this the data for the 31 languages were added [https://github.com/open-dict-data/ipa-dict/](ipa dict files)
* [CC0: Public Domain] Chinese/Mandarin-IPA language sentence pairs were generated:
  - from the chinese sentences taken from dataset [https://www.kaggle.com/datasets/concyclics/machine-translation-chinese-and-english](from kaggle)
  - based on the above dictionary and MISTRAL-nemo made IPA dictionary which was paired with chinese sentences to ipa sentences using string substitution.
* [Apache-2.0] Wikipron data were added for selected large languages [https://github.com/CUNY-CL/wikipron/tree/master/data/scrape/tsv](from wikipron data)
* [cc-by-nc-4.0] Tibetan taken from [https://huggingface.co/datasets/billingsmoore/tibetan-phonetic-transliteration-dataset](billingsmoore)
* [MIT/Apache2] Slovak language is mostly self made, I hereby dedicate it under MIT/Apache2
* [CC-BY-SA 3.0]: Text in Japanese corpus is licensed as follows. The text data were modified and pronunciation information is added. basic5000 is as follows:
  - wikipedia (https://ja.wikipedia.org/) CC-BY-SA 3.0
  - TANAKA corpus (http://www.edrdg.org/wiki/index.php/Tanaka_Corpus) CC-BY 2.0
  - JSUT (Japanese speech corpus of Saruwatari-lab., University of Tokyo) (https://sites.google.com/site/shinnosuketakamichi/publication/jsut). CC-BY-SA 4.0

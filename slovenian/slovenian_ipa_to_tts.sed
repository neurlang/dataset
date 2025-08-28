# Convert Slovenian IPA diacritics to TTS-friendly Contour Tones
# This script handles vowels with pitch accent diacritics.

# 1. Convert rising tone grave accent (à, è, ì, ò, ù, ə̀) to Low-High contour (˩˥)
s/à/a˩˥/g
s/è/e˩˥/g
s/ì/i˩˥/g
s/ò/o˩˥/g
s/ù/u˩˥/g
s/ə̀/ə˩˥/g

# 2. Convert falling tone acute accent (á, é, í, ó, ú, ə́) to High-Low contour (˥˩)
s/á/a˥˩/g
s/é/e˥˩/g
s/í/i˥˩/g
s/ó/o˥˩/g
s/ú/u˥˩/g
s/ə́/ə˥˩/g

# 3. Handle the circumflex (î) for short falling tone
# 'î' is a common notation for a short /i/ with a falling tone.
s/î/i˥˩/g

# 4. Handle the breve (ă) for a short central vowel, typically /ə/
# The breve itself denotes shortness. If it needs a tone, it must be specified.
# Since your example did not specify a tone on 'ă', we map it to a short, toneless schwa.
# If you find 'ă' with a diacritic (e.g., ắ, ằ), add rules for them.
s/ă/ə/g

# 5. Handle the specific sequences found in the lexicon
# 'ɔ̀' and 'ɔ́' are likely representations of a rounded open-mid back vowel with tone.
# Standard Slovenian uses /ɔ/ (without rounding diacritic), so we map to /o/ with the appropriate tone.
s/ɔ̀/o˩˥/g
s/ɔ́/o˥˩/g

# 'òó' and 'ìíî' are sequences of two/three vowels, each with a diacritic.
# This almost certainly represents a single syllable nucleus with a complex contour.
# The most common analysis for, e.g., 'òó' is a long rising-falling tone.
# We represent this as a sequence of three level tones: Low-High-Mid (˩˥˧) or Low-High-Low (˩˥˩).
# ˩˥˧ is chosen as a more natural, less jarring contour for the TTS engine.
s/òó/o˩˥˧/g
s/ìíî/i˩˥˧/g

# 'ă' is a breve, denoting a short vowel. Slovenian has short falling tones.
# The sequence 'ăàá' is highly unusual and likely represents a very short vowel with a complex pitch.
# The most logical interpretation is a short, sharply falling tone.
# We represent this as a high-low contour on a short vowel: ˥˩ (the lack of a length mark 'ː' will keep it short)
s/ăàá/a˥˩/g

# 'èé' is analogous to 'òó' - a long vowel with a rising-falling contour.
s/èé/e˩˥˧/g

# conversion script from TSV manually created based on WikipediaHomographData to our multi.tsv homograph format
import re
from collections import defaultdict

def clean_text(text):
    """Remove all punctuation and normalize whitespace, turn - and / and _ into word separator"""
    text = text.replace('-', ' ')
    text = text.replace('/', ' ')
    text = text.replace('_', ' ')
    return re.sub(r'[^\w\s]', '', text).strip()

# Load lookup data (word->IPA) manually done in libre office calc
lookup = defaultdict(dict)
with open('WikipediaHomographData/lookup.tsv', 'r') as f:
    for line in f:
        if not line or '\t' not in line:
            continue  # Skip empty or malformed lines
        key, ipa = line.strip().split('\t')
        lookup[key] = ipa

# Process allmulti.tsv (manually done in libre office calc) and generate output
with open('WikipediaHomographData/allmulti.tsv', 'r') as fin, open('output.tsv', 'w') as fout:
    for line in fin:
        parts = line.strip().split('\t')
        if len(parts) < 3:
            continue
            
        homograph, key, sentence = parts[0], parts[1], parts[2]
        
        # Clean and split sentence
        cleaned = clean_text(sentence)
        words = cleaned.split()
        
        # Clean homograph for matching
        clean_homograph = clean_text(homograph)
        
        # Prepare replacements
        output = []
        matches = 0
        for word in words:
            # Compare cleaned word with cleaned homograph
            if clean_text(word) == clean_homograph:
                output.append(lookup[key])
                matches += 1
            else:
                output.append('_')
        
        # Validate and write output
        if matches > 0:
            clean_sentence = ' '.join(words)
            output_line = f"{clean_sentence}\t{' '.join(output)}"
            fout.write(output_line + '\n')
        else:
            print(f"Skipped sentence: {sentence} (found {matches} matches), but no homograph {homograph}")

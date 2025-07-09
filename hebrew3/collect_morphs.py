# Initialize an empty dictionary
morph_dict = {}

# Open the file
with open('morphs_uniq.tsv', encoding='utf-8') as f:
    for line in f:
        # Split by any whitespace (spaces or tabs)
        parts = line.strip().split()
        if len(parts) >= 2:
            value = parts[-1]    # The 'M...' value
            key = parts[1]   # The word, e.g., 'foo'
            morph_dict[key] = value
            #print(f"{key}\t{value}")

# Loop over the dictionary and print
for key, value in morph_dict.items():
     print(f"{key}\t{value}")

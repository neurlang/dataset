from datasets import load_dataset

# The entire dataset is available for use
dataset = load_dataset("sarahwei/Taiwanese-Minnan-Example-Sentences")

for row in dataset['train']:
	print(row['chinese'], "TABULATOR", row['minnan roman'])


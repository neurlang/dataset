import json

#♻️ Misaki to espeak
def to_espeak(ps):
    # Optionally, you can add a tie character in between the 2 replacement characters.
    ps = ps.replace('ʤ', 'dʒ').replace('ʧ', 'tʃ')
    ps = ps.replace('A', 'eɪ').replace('I', 'aɪ').replace('Y', 'ɔɪ')
    ps = ps.replace('O', 'oʊ').replace('Q', 'əʊ').replace('W', 'aʊ')
    return ps.replace('ᵊ', 'ə')


def convert_json_to_tsv(json_data):
    tsv_lines = []
    for key, value in json_data.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
              if sub_value is not None:
                if sub_key == "DEFAULT":
                    tsv_lines.append(f"{key.lower()}\t{to_espeak(sub_value)}")
                else:
                    tsv_lines.append(f"{key.lower()}\t{to_espeak(sub_value)}\t[\"{sub_key.lower()}\"]")
        elif value is not None:
            tsv_lines.append(f"{key.lower()}\t{to_espeak(value)}")
    return tsv_lines

def main(filename):
    # Load JSON data from the file
    with open(filename, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    # Convert JSON to TSV
    tsv_lines = convert_json_to_tsv(json_data)

    # Write TSV to a file
    with open('lexicon.tsv', 'a', encoding='utf-8') as f:
        for line in tsv_lines:
            f.write(line + '\n')

if __name__ == "__main__":
    main('us_silver.json')
    main('us_gold.json')

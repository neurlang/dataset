import re
import sys

def expand_homographs(input_file, output_file):
    """
    Process a TSV file and expand homographs into multiple rows.
    
    Args:
        input_file: Path to input TSV file
        output_file: Path to output TSV file with expanded rows
    """
    # Regular expression to find pronunciations in square brackets
    bracket_re = re.compile(r'\[([^\]]+)\]')
    
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        
        for line in infile:
            line = line.strip()
            if not line:
                continue
                
            parts = line.split('\t')
            if len(parts) != 2:
                outfile.write(line + '\n')
                continue
                
            word, pronunciation = parts
            # Find all pronunciations in square brackets
            bracket_matches = bracket_re.findall(pronunciation)
            
            if not bracket_matches:
                # No brackets found, write original line
                outfile.write(line + '\n')
                continue
                
            # Get the base pronunciation (outside brackets)
            base_pronunciation = bracket_re.sub('', pronunciation).strip()
            if base_pronunciation:
                outfile.write(f'{word}\t{base_pronunciation}\n')
                
            # Write each bracketed pronunciation as a separate row
            for match in bracket_matches[0].split('['):  # Handle multiple brackets if needed
                for pron in match.split(']')[0].split('|'):  # Split by | if multiple options
                    pron = pron.strip()
                    if pron:
                        outfile.write(f'{word}\t{pron}\n')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python expand_homographs.py <input.tsv> <output.tsv>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    expand_homographs(input_file, output_file)
    print(f"Processed {input_file} and wrote expanded homographs to {output_file}")

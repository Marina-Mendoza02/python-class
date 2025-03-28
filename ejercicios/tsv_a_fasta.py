
input_file = "dna_sequences.txt"
output_file = "dna_sequence.fa"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        id, seq = line.strip().split("\t")
        outfile.write(f">{id}\n{seq.upper()}\n")
        
        
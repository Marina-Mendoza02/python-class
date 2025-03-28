
inputfile = "dna_sequence.fa"

with open(inputfile, "r") as infile:
    lines = infile.readlines()

# print(lines[0])
# print(lines[1])

filtered_lines = [line for line in lines if line.startswith(">")]
print(f"Sequence total: {len(filtered_lines)}")


def count_bases(dna):
    bases = "ATGC"
    for base in dna:
        num_bases = dna.upper().count(base)
        print(f"base {num_bases}")

count_bases = "GTCGACATATACGACGA"
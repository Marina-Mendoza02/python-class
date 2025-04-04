
secuencia = tuple("ATGCTTCGA")

# Forma 1
# print(secuencia.count("T"))
# print(secuencia.count("G"))
# print(secuencia.count("C"))

# Forma 2
# bases = list("ATGCTTCGA")
# freq = [(base, secuencia.count(base)) for base in bases]
# print(freq)

# Forma 3 ciclos
for base in "ATGCTTCGA":
    print(f"{secuencia.count(base)} bases {base}")


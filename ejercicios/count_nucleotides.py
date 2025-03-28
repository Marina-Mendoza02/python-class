
secuencias = input("Dame secuencias separadas por comas: ").upper().split(",")

conteo = [[f"A: {secuencia.count('A')}", secuencia.count("T"), secuencia.count("G"), secuencia.count("C")]  for secuencia in secuencias]

print(conteo)
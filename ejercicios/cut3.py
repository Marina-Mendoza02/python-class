secuencias = input("Dame las secuencias separadas por comas: ").split(",")

codones_inicio = [secuencia.strip()[:3] for secuencia in secuencias]

print(codones_inicio)
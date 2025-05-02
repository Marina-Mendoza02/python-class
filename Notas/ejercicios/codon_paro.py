
codones_parada = {"TAA", "TAG", "TGA"}
secuencias = input("Dame secuencias separadas por comas: ").split(",")

secuencias_con_stop = [secuencia for secuencia in secuencias if "TAA" in secuencia or "TAG" in secuencia or "TGA" in secuencia]


print(secuencias_con_stop)

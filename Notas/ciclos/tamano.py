with open("genes.gff") as file:
    for line in file:
        columns = line.strip().split("\t")
        tamano = int(columns[4]) - int(columns[3])+1
        print(tamano)



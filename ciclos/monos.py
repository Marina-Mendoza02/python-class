
apes = ["Pongo pygmaeus", "Pan troglodytes", "Gorilla gorilla"]

for ape in apes:
    name_length = len(ape)
    first_letter = ape[0]

    print(f"{ape} is an ape. Its name starts with {ape[0]}")
    #print(f"{ape} is an ape. Its name starts with {first_letter}")
    #print(ape + "is an ape. Its name starts with " + first_letter)
    print(f"Its name has {len(ape)} letters")
    #print(f"Its name has {name_length} letters")
    #print("Its name has " + str(name_length))
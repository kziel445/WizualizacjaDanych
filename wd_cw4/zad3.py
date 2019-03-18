with open("plik2.txt","w+") as plik:
    plik.write("Piszu piszu\n")
    plik.write("Magediszu\n")
    plik.write("Mokolele\n")

with open("plik2.txt", "r") as plik:
    linia=plik.readline()
    print(linia)
    while True:
        line = plik.readline()
        print(line)
        if not line:
            break
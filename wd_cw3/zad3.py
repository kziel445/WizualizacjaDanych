produkty1={"Jajko":"sztuki",
           "Bulka":"gramy",
           "Mleko":"litry"}
zmiana=[key for key,value in produkty1.items() if value=="sztuki"]
print("Oryginalny słownik")
print(produkty1)
print("Słownik zmieniony")
print(zmiana)

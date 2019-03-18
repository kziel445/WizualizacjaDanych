import random

lista=[]

for i in range (0,4):
    x=random.randint(1,101)
    lista.append(x)
print(lista)

lista2= " ".join(map(str,lista))
print(lista2)

plik=open("plik1.txt","w")
plik.write(lista2)
plik.close()
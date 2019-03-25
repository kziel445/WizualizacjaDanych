import random

lista=[]
for i in range (0,10):
    x=random.randint(1,101)
    lista.append(x)
lista.sort(reverse=True)
print(lista)

lista2=" ".join(map(str,lista))
with open("plik.txt","w+") as plik:
    plik.write(lista2)
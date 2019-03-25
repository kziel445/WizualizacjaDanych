import random
def secmax(lis):
    max=0
    max2=0
    for i in lista:
        if (i >= max):
            max2 = max
            max = i

        elif (i < max and i > max2):
            max2 = i
    print("Druga najwieksza wartoscia jest: %i" % (max2))

lista=[]
for i in range (0,4):
    x=random.randint(1,101)
    lista.append(x)
print(lista)
secmax(lista)
import math
def mono(a,b):
    if(a>0):
        print("Funkcja jest rosnaca")
        return 1
    elif(a == 0):
        print("Funkcja jest stala")
        return 0
    elif(a<0):
        print("Funkcja jest malejaca")
        return -1

print(mono(2,3))
print(mono(0,3))
print(mono(-4,3))

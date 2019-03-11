import random
macierz=[[random.randint(0,100) if x==y else 0 for x in range(4)] for y in range(4)]
print(macierz)
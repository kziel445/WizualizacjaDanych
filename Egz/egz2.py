import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def suma(x):
    wynik = 0
    for i in range(1,x+1):
        wynik += i
    return wynik
print(str(suma(10)) + ' ' + str(suma(123)))

liczby = np.arange(256,348)
liczby2 = [i for i in range(256,348) if i%13==0]
print(liczby2)

"""slowo = input("Podaj palindrom: ")
x = len(slowo)
i = 0
while i<x:
    if(slowo[i]!=slowo[x-1]):
        print("Slowo NIE JEST palindromem")
        break
    x -= 1
    i += 1
    if(i>=x):
        print("Slowo JEST palindromem")"""
x = np.arange(-10,11,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()




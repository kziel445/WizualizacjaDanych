import numpy as np
import matplotlib.pyplot as plt

"""losowana_macierz= np.random.randint(0,10,(5,5))
print(losowana_macierz)

jedynki = np.ones([5,5])
print(jedynki==1)

ciag = np.arange(1,11,1)
print(ciag[ciag%2==0])

tablica1 = np.random.randint(1,10,(2,4))
tablica2 = np.random.randint(1,10,(2,4))
print(tablica1)
print(tablica2)
tablica_polaczona = np.concatenate((tablica1,tablica2))
print(tablica_polaczona)

tablica1 = np.random.randint(1,10,(4,2))
tablica2 = np.random.randint(1,10,(4,2))
print(tablica1)
print(tablica2)
tablica_polaczona = np.concatenate((tablica1,tablica2),axis=1)
print(tablica_polaczona)

macierz = np.random.randint(0,11,(3,3))
kolejnosc = [2,1,0]
print(macierz)
print(macierz[kolejnosc])
print(macierz[:,kolejnosc])"""

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
unikalne = np.unique(iris[:,4], return_counts=True)

#print(unikalne)
#print(np.asarray((unikalne)))
print(iris.max(axis = 0))
print(iris.min(axis = 0))
numeryczna = np.delete(iris,4,1).astype(float)
#print(numeryczna)
tekstowa = iris[:,[4]]
print(tekstowa)


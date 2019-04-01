#zadanie 1-3
import numpy as np

def tablicjusz(n):
    print(np.arange(1,n*n+1,1))
    return
#1
a = np.arange(2,21,2)
print(a)

#2
b = a.astype('float')
print(b)
c = b.astype('int64')
print(c)

#3
n=1
tablicjusz(n)
#4
import numpy as np
def coo(baza,potega):

    return np.logspace(1.0, potega, num=potega, base=baza)

print(coo(2,4))

#print(np.logspace(1.0,5.0,num=5,base=2))
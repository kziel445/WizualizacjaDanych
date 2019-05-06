import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0,30,0.1)
s = np.sin(x)
c = np.cos(x)
s1 = np.sin(x-math.pi)+2
plt.title("Wykres sin(x), sin(x-pi)+2 i cos(x)")
plt.plot(x,s,label='sin(x)')
plt.plot(x,c,label='cos(x)')
plt.plot(x,s1,label='sin(x-pi)+2')

plt.ylabel("y")
plt.xlabel("x")
plt.legend()
plt.show()

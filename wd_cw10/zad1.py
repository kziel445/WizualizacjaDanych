import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,20,20)
plt.title("Wykres funckji f(x) dla x [1,20]")
plt.plot(x,1/x, 'g^:',label='f(x)=1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([0,20,0,1])
plt.legend()
plt.show()

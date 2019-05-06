import matplotlib.pyplot as plt
import numpy as np

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = data['a'] - data['b']



plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()
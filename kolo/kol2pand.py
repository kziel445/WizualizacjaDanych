import pandas as pd
import string
import numpy as np

ascii_m = list(string.ascii_lowercase)
ascii_d = list(string.ascii_uppercase)


duze_ascii = pd.DataFrame(pd.Series(ascii_d,np.arange(0,26,1)),columns=['duze'])
male_ascii = pd.DataFrame(pd.Series(ascii_m,np.arange(0,26,1)),columns=['male'])
ascii = pd.merge(male_ascii,duze_ascii,left_index = True,right_index = True)
print(ascii)

df = pd.read_csv('zamowienia.csv',sep=';')
utarg = df[(df.Kraj == 'Polska') | (df.Kraj == 'Niemcy')].sort_values(by=['Utarg'],ascending = False).groupby('Kraj').head(3)
print(utarg)


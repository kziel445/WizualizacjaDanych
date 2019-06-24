import pandas as pd
import numpy as np
class czas:
    def __init__(self,godzina,minuta):
        self.godzina = godzina
        self.minuta = minuta
def zegar(czas):
    if(czas.minuta<10):
        czas.minuta="0" + str(czas.minuta)
    print(str(czas.godzina) +":"+ str(czas.minuta))
slownik = {i :i*i for i in range(99)}
for x in list(slownik)[94:99]:
    print(slownik[x])
zegar(czas(2,10))

df = pd.read_csv("przepis.csv",sep="#")
df = df.set_index(df['Składnik'])
df = df.drop(columns=['Składnik'],axis=0)

df2 = pd.DataFrame([[10,'Sól'],[20,'Jajka']])
df2.columns=['Waga w g','Składniki']
df2 = df2.set_index(df2['Składniki'])
df2 = df2.drop(columns=['Składniki'])
df = df.append(df2)

print(df)


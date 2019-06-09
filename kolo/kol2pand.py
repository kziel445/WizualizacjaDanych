import pandas as pd
import string
import numpy as np
import matplotlib.pyplot as plt

ascii_m = list(string.ascii_lowercase)
ascii_d = list(string.ascii_uppercase)


duze_ascii = pd.DataFrame(pd.Series(ascii_d,np.arange(0,26,1)),columns=['duze'])
male_ascii = pd.DataFrame(pd.Series(ascii_m,np.arange(0,26,1)),columns=['male'])
ascii = pd.merge(male_ascii,duze_ascii,left_index = True,right_index = True)
#print(ascii)

df = pd.read_csv('zamowienia.csv',sep=';')
utarg = df[(df.Kraj == 'Polska') | (df.Kraj == 'Niemcy')].sort_values(by=['Utarg'],ascending = False).groupby('Kraj').head(3)
#print(utarg)

xlsx = pd.ExcelFile('Najpopularniejsze-imiona-w-Polsce-w-latach-2000-2017.xlsx')
df = pd.read_excel(xlsx, 'Arkusz1')
#print(df[(df['Plec'] == 'M') | (df['Plec'] == 'K')].groupby(['Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'), ascending=False).head(6))
kobiety = df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'), ascending=False).head(3)
mezczyzni = df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'), ascending=False).head(3)


x = df['Rok'].unique()
    # bez funkcji flatten matplotlib wyrzuca wyjÄtek, ktĂłry informuje nas, Ĺźe nie moĹźna
    # przekazywaÄ parametru jako tablicy wielowymiarowej a w takiej postaci w tym przypadku
    # zwracany jest wektor y, korzystamy wiÄc z flatten() poznanej przy okazji omawiania biblioteki numpy
y = df.groupby('Rok').agg({'Liczba':['sum']}).values.flatten()
plt.bar(x, y)

    # wyĹwietlamy caĹy wykres
    #10 zestaw
plt.show()

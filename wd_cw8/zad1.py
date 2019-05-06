import xlrd
import openpyxl
import pandas as pd
import numpy as np
#zad1
xlsx = pd.ExcelFile(r'D:\isi7\Python\1cwiczenia\wd_cw8\imiona.xlsx')
df = pd.read_excel(xlsx)

#zad2.1
#print (df[df['Liczba']>1000])
#zad2.2
#print(df[df['Imie']==('KAMIL')])
#zad2.3
#print(df.agg({'Liczba':'sum'}))
#zad2.4
print(df[((df.Rok >= 2000) & (df.Rok<=2005))].agg({'Liczba':'sum'}))
#zad2.5
#print(df.groupby(['Plec']).agg({'Liczba':['sum']}))
#zad2.6
#print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())
#zad2.7
#print(df.groupby(['Plec', 'Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'), ascending=False).iloc[[0,1]])

#zad3
#file = open('zamowienia (1).csv')
#df = pd.read_csv(file, delimiter=';')
# print(df)
#zad3.1

#zad3.2

#zad3.3

#zad3.4
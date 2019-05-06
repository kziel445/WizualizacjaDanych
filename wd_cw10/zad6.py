import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile(r'D:\isi7\Python\1cwiczenia\wd_cw8\imiona.xlsx')
df = pd.read_excel(xlsx)
Kob = df[df['Plec']==('K')].agg({'Liczba':['sum']})
Men = df[df['Plec']==('M')].agg({'Liczba':['sum']})
lista = df.groupby(['Plec']).agg({'Liczba':['sum']})
etykiety = ['K','M']
wartosci = [Kob.iat[0,0],Men.iat[0,0]]
plt.subplot(1,3,1)
plt.bar(etykiety,wartosci)
plt.subplot(1,3,2)

plt.subplot(1,3,3)
plt.show()




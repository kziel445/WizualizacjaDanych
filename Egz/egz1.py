import pandas as pd
import matplotlib.pyplot as plt
class Kierownik:
    def __init__(self,Imie,Nazwisko,staz):
        self.Imie = Imie
        self.Nazwisko = Nazwisko
        self.pensja = 3200 + staz*250
        self.staz = staz
    def info(self):
        print("# " + self.Imie + " # " + self.Nazwisko + " # " + str(self.pensja) + " # " + str(self.staz) + " #")\

def wielomian(wspolczynniki,x):
    w = 0
    for i in range(len(wspolczynniki)):
        w = w + wspolczynniki[i] * x**i
      #  w = w + wspolczynniki[i] * x**i
    return w


ktos= Kierownik('Kamil','Zieiński',4)
ktos1= Kierownik('Ser','Buła',3)
print(ktos.info())
print(ktos1.info())

lista1 = [2,3,4,5]
print(lista1)
print(wielomian(lista1,2))

lista = [x for x in range(1,8)]
lista = []


answer = [[i*j for i in range(1,8)] for j in range(1,8)]
#print(answer)

df = pd.read_csv("miasta.csv",sep = ';')
df['Gestosc']=['%.2f'%(float(df.Ludnosc[i].replace(" ",""))/float(df.Powierzchnia[i].replace(",","."))) for i in df.index.values]
df['Powierzchnia']=[float(df.Powierzchnia[i].replace(",",".")) for i in df.index.values]
df['Ludnosc']=[float(df.Ludnosc[i].replace(" ","")) for i in df.index.values]
#print(df)
#print(df.loc[df['Powierzchnia'].idxmin()])
#print(df[df['Ludnosc']>500000])
plt.pie(df['Gestosc'],labels = df['Miasta'],shadow = True,autopct = '%1.1f%%',explode= (0.1,0,0,0,0))
plt.title("kanapka")
#plt.show()

df2 = pd.DataFrame([['Gdansk',261.96,466631.0,''],['Gdansk2',262,466631.0,''],['Gdansk3',2,466631.0,'']],columns = df.columns.values)

df2['Gestosc']=['%.2f'%(float(df2.Ludnosc[i])/float(df2.Powierzchnia[i])) for i in df2.index.values]

#print(df.append(df2,ignore_index=True))

dfp = pd.read_csv('ludnosc.csv',sep=';')
dfp.columns = dfp.loc[1]
dfp.drop(dfp.index[[1,4]])
print(dfp)

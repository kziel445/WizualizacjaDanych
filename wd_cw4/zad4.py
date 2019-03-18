class NaZakupy:
    def __init__(self,nazwa,ilosc,miara,cena):
        self.nazwa=nazwa
        self.ilosc=ilosc
        self.miara=miara
        self.cena=cena
    def ile_kosztuje(self):
        return str(self.ilosc * self.cena) + "zł"

    def wyswietl_produkt(self):
        return self.nazwa+ " " + str(self.ilosc) + self.miara + " " + str(self.cena) + "zl"

Ziemniaki =NaZakupy("Ziemniaki",10,"kg",3)
print(NaZakupy.wyswietl_produkt(Ziemniaki))
print(NaZakupy.ile_kosztuje(Ziemniaki))
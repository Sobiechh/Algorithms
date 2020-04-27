import string

class CEZARY:
    def __init__(self, tab):
        self.tab = tab.upper()

    def cezary(self, text):
        klucz = 1
        alfabet = string.ascii_uppercase
        kod = alfabet[klucz:] + alfabet[:klucz]
        tabela = str.maketrans(alfabet, kod)
        return text.translate(tabela)

    def cezary_u(self, text):
        klucz = 1
        alfabet = string.ascii_uppercase
        kod = alfabet[:klucz] + alfabet[klucz:]
        tabela = str.maketrans(alfabet, kod)
        return text.translate(tabela)

    def __str__(self):
        wynik = "Słowo: "+self.tab +"\n"
        wynik+= "Zaszyfrowane: " + self.cezary(self.tab) + "\n"
        wynik += "Odszyfrowane: " + self.cezary_u(self.tab) + "\n\n"
        return wynik


file = open('cezar_in.txt','r')
linia = file.readline()
dane = []
while linia:
    dane.append(linia.strip())
    linia=file.readline()

for tekst in dane:
    print(CEZARY(tekst), end = " ")
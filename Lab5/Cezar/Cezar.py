KLUCZ = 8


def szyfruj(txt):
    zakodowany = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - KLUCZ:
            zakodowany += chr(ord(txt[i]) + KLUCZ - 26)
        else:
            zakodowany += chr(ord(txt[i]) + KLUCZ)
    return zakodowany


tekst = input("Podaj ciąg do zaszyfrowania:\n")
print("Ciąg zaszyfrowany:\n", szyfruj(tekst))
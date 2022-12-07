# Funkcja ord() - zwraca kod ascii dla danego znaku
# print(ord("A"))
# print(ord("B"))
# print(ord("Z"))

# Funkcja chr() - zwraca znak dla danego kodu ascii
# print(chr(65))
# print(chr(75))
# print(chr(89))

# można łączyć....
# print(chr(ord("C")))
# print(chr(ord("C")+1))

# napisz alfabet za pomocą pętli for
# liter od 65 do 90 jest 26.
# for i in range(65,91):
#     print(chr(i), end="")

# jak wydobyć literki z napisu...
# napis = "POLSKA"
# print(len(napis))
# print(napis[0])
# print(napis[1])

# napisz petle wyciągającą z napisu literki

# napis = input()
# for i in range(len(napis)):
#     print(napis[i])

# napisz pętle wyciągającą kody ascii z napisu

# napis = input()
# for i in range(len(napis)):
#     print(ord(napis[i]))

# zaszyfruj napis Cezarem w kluczu = 3

napis = input()
szyfr = ""
for i in range(len(napis)):
    szyfr = szyfr + chr( 65 + (ord(napis[i]) - 65 + 3) % 26)
print(napis, szyfr)
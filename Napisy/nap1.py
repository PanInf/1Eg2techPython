# s = input()
# napis (string) to jakby "lista", więc działa foreach i for z range
# for x in s:
#     print(x)

# for i in range(len(s)):
#     print(s[i])

# napis to nie jest lista sensu stricte
# L = [7,4,5,2]

# L.sort()
# s.Sort() - to byłby błąd! Napis to nie jest "pełna" lista
# print(s, L)

# przechodzenie z napisu w liste i z listy w napis

# L = list(s)
# print(L)
# L.sort()
# print(L)
# w = "".join(L)
# print(w)

# sprawdź czy wpisne słowo jest palindromem

# s = input()
# L = list(s)
# R = L.copy()
# R.reverse()
# print(L, R)
# if L == R:
#     print("jest palindromem")
# else:
#     print("nie jest palindromem")

# sprawdzenie palindroma za pomocą listy

# s = input()

# for i in range(len(s)//2):
#     if s[i] != s[len(s)-1-i]:  
#     # s[:i+1] != s[:len(s)-1-i:-1]
#         exit("NIE")
# exit("TAK")

L = [ i**2 for i in range(1,10)]
print(L)
# L[start:stop:step]
print(L[:4])
print(L[::2])
print(L[1::2])
print(L[::-1])

print(L[1:6:2])
print(L[1:6:-2])
print(L[6:1:-2])
print(L[:1:-2])



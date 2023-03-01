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

s = input()
L = list(s)
R = L.copy()
R.reverse()
print(L, R)
if L == R:
    print("jest palindromem")
else:
    print("nie jest palindromem")

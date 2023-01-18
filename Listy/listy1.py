# x = list(range(5))
# for item in x:
#     print(item)

# for item2 in range(4):
#     print(item2)

# print(len(x))

# for i in range(len(x)):
#     print(x[i])


# deklaracja listy i iteracja po liście:

# L = [3, 5, 8, 13, 17, 27]

# for elem in L:
#     print(elem, end=" ")

# print("\n")

# for i in range(len(L)):
#     print(L[i], end=" ")


# funkcje w listach

K = [4, 7, 5, 7, 3, 3, 2, 8, 7]
print(K)

K.append(3)
print(K)
print(K.count(7))
print(K.index(7))
K.insert(2,4)
print(K)
# pytanie - jak wstawić "4" na koniec listy?
# K.insert(len(K),4) # lub po prostu append()
# print(K)
K.pop()  # pop() domyślnie usuwa ostatnią, albo podaną
print(K)
# K.reverse()
# print(K)
# K.sort() # lub sort(reverse=True) malejąco
# print(K)

# Zadanie - usuń z listy wszystkie 7
# for i in range(K.count(7)):
#     K.remove(7)
# print(K)

for i in range(K.count(7)):
    K.pop(K.index(7))
print(K)


# poszukaj maksa w tablicy 2/3 metodami

# print(max(K))


# maksik = K[0]
# for i in K:
#     if i > maksik:
#         maksik = i
# print(maksik)


# maksik = K[0]
# for i in range(len(K)):
#     if K[i] > maksik:
#         maksik = K[i]
# print(maksik)

# Zakresy w listach
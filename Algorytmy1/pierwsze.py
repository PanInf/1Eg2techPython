# 1. Algorytm sprawdzający czy liczba jest pierwsza
# liczba pierwsza dzieli sie tylko przez 1 i samą siebie
# 2, 3, 5, 7, 11, 13, 17, 19 itd...
# liczba x ma swój dzielnik (o ile go ma) w przedziale [2, sqrt(x)]

# WERSJA 1
# n = int(input())
# for i in range(2, n):
#     if n % i == 0:
#         print("Liczba nie jest pierwsza")
#         exit(0)
# print("Liczba jest pierwsza")

# WERSJA 2
# n = int(input())
# flaga = True
# for i in range(2, n):
#     if n % i == 0:
#         flaga = False
# if flaga == True:
#     print("Liczba jest pierwsza")
# else:
#     print("Liczba nie jest pierwsza")

# WERSJA 3 (dla chętnych - funkcja)

# def czyPierwsza(n):
#     flaga = True
#     for i in range(2, n):
#         if n % i == 0:
#             flaga = False
#     return flaga


# WERSJA 4
from math import sqrt
n = int(input())
for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
        print("Liczba nie jest pierwsza")
        exit(0)
print("Liczba jest pierwsza")

# 2. Generator liczb pierwszych - liczby pierwsze w przedziale [p, q]



# 3. Generator liczb pierwszych - początkowe k liczb pierwszych
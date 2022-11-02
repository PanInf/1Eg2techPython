# Zad 1
# n = int(input())

# for i in range(n):
#     print("*-|", end="")

# Zad 2 PRE

# print("Bartosz"*2)
# print("*"*5)

# Zad 2

# n = int(input())
# for i in range(1, n+1):
#     print("*"*i, end="")
#     if i%2 == 1:
#         print("||",end="")
#     else:
#         print("--",end="")

# Zad 3

# n = int(input())
# for i in range(1, n+1):
#     print("*", end="")
#     if i % 2 == 1:
#         print("|"*i, end="")
#     else:
#         print("-"*i, end="")

# PRE - Tabliczka mnożenia

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end="\t")
#     print()

# PRE na 2 pętle:

# *
# **
# ***
# ****

# ****
# ***
# **
# *

#    *
#   **
#  ***
# ****

# ****
#  ***
#   **
#    *

n = int(input())

for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()

print()
print()

for i in range(n):
    for j in range(n - i):
        print("*", end="")
    print()

print()
print()

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(n - i - 1, n):
        print("*", end="")
    print()

print()
print()

for i in range(n):
    for j in range(i):
        print(" ", end="")
    for k in range(i, n):
        print("*", end="")
    print()
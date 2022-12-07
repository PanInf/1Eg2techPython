a,b,c,d = int(input()), int(input()), int(input()), int(input())

x = b
y = d
iloczyn = x*y
while y>0:
    x, y = y, x%y
nww = iloczyn // x

e = (nww // b) * a
f = (nww // d) * c
g = e + f

print(f"{a}/{b} + {c}/{d} = {e}/{nww} + {f}/{nww} = {g}/{nww}")

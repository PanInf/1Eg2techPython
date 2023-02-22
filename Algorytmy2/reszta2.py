x = int(input())
T = [50,20,10,5,2,1]
W = []
for i in T:
    ilosc = x // i
    if ilosc > 0:
        x = x - ilosc * i
        for j in range(ilosc):
            W.append(i)
        # opcjonalnie zamiast appenda w forze: W = W + ilosc*[i]
print(W)


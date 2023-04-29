n = int(input())
for i in range(3):
    g = (int(n/10)*10)
    frac = n - g
    print(frac)
    n = int(n/10)

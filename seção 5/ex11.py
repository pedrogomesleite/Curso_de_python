n = int(input())
if n < 0:
    print('Número invalido!')
else:
    s = 0
    while n > 0:
        c = n/10 - int(n/10)
        s += c
        n = int(n/10)
    s = int(s*10)
    print(s)

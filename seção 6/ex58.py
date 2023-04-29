a = int(input('a:'))
b = int(input('b:'))
soma = 0
for i in range(a, b+1):
    for j in range(2, i+1):
        if j == i:
            soma += i
        if i % j == 0:
            break
print(soma)

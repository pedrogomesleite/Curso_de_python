n = int(input())
soma = 0
for i in range(2, n+1):
    for j in range(2, i+1):
        if j == i:
            soma += i
        if i % j == 0:
            break
print(soma)

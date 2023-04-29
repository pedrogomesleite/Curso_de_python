
soma = 0
for i in range(1, 2_000_000):
    for j in range(2, i+1):
        if j == i:
            soma += i
        if i % j == 0:
            break
print(soma)

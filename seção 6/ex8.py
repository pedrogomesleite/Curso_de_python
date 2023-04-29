maior = 0
menor = 0
for i in range(10):
    n = int(input())
    if n < menor or i == 0:
        menor = n
    if n > maior or i == 0:
        maior = n
print(f'maior:{maior}')
print(f'menor:{menor}')

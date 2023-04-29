cont = 0
m = 0
maior = 0
menor = 0
mp = 0
p = 0
soma = 0
while True:
    n = int(input("digite:"))
    if n == 0:
        break
    soma += n
    cont += 1
    m += n
    if n > maior or cont == 1:
        maior = n
    if n < menor or cont == 1:
        menor = n
    if n % 2 == 0:
        mp += n
        p += 1
print(f'soma:{soma}')
print(f'qtd numeros:{cont}')
print(f'Média:{m/cont}')
print(f'maior:{maior}')
print(f'menor:{menor}')
print(f'média pares:{mp/p}')
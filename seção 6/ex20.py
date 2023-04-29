contp = 0
contn = 0
while True:
    n = int(input())
    contn += 1
    if n == 1000:
        break
    if n % 2 == 0:
        contp += 1

print(f'qtd de pares:{contp},qtd numeros lidos:{contn}')

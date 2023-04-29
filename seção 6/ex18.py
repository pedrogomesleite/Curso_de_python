cont = 0
maior = 0
n = int(input())
for i in range(n):
    num = int(input())
    if num > maior or i == 0:
        maior = num
        cont += 1
print(f'maior:{maior},quantidade de vezes:{cont}')

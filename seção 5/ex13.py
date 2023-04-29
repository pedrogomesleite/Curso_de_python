
prova1 = float(input('prova 1:'))
prova2 = float(input('prova 2:'))
prova3 = float(input('prova 3:'))
r = (prova1*1 + prova2*1 + prova3*2) / 4
print(f'Média ponderada das notas:{r}')
if r >= 60:
    print('Aprovado!')
else:
    print('Reprovado!')
nota1 = float(input())
nota2 = float(input())

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print('nota invaliada\n')
    print('uma nota deve estar entre 0:10')
else:
    print(f'média={(nota1+nota2)/2}')

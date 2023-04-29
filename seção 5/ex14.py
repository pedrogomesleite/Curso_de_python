tl = float(input('trabalho laboratório:'))
av = float(input('avaliação semestral:'))
ef = float(input('Exame final:'))

r = (tl*2 + av*3 + ef*5) / 10

if r < 3:
    print('Reprovado!')
elif r < 5:
    print('Recuperação!')
else:
    print('Aprovado!')
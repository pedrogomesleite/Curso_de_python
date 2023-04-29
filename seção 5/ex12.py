import math

n = int(input())
if n < 0:
    print('Número inválido!')
else:
    print(f'Log={math.log10(n)}')

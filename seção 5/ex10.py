alt = float(input("altura:"))
sexo = input('sexo (m/h):')

if sexo == 'm':
    print(f'peso ideal={(72.7*alt)-58}')
else:
    print(f'peso ideal={(62.1 * alt) - 44.7}')

n = int(input())
final = ''
cont = 0
for i in range(0, n):
    cont = 0
    final = ''
    palavra = list(str(input()))
    for letra in palavra:
        if (ord(letra) >= 65 and ord(letra) <= 90) or (ord(letra) <= 122 and ord(letra) >= 97 ):
            letra = str(chr(ord(letra) + 3))
        final = final + letra
        cont += 1
    final = list(final[::-1])
    for j in range(int(cont/2), cont):
        final[j] = str(chr(ord(final[j]) - 1))
    final = ''.join(final)
    print(final)


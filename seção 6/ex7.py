media = 0
for i in range(10):
    m = int(input())
    if m < 0:
        m = int(input('Digite um valor valido!'))
    media += m
media = media/10
print(media)

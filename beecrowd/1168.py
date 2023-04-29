n = int(input())
for i in range(0, n):
    v = str(input())
    sum = 0
    for num in v:
        if num == '1':
            sum += 2
        elif num == '2':
            sum += 5
        elif num == '3':
            sum += 5
        elif num == '4':
            sum += 4
        elif num == '5':
            sum += 5
        elif num == '6':
            sum += 6
        elif num == '7':
            sum += 3
        elif num == '8':
            sum += 7
        elif num == '9':
            sum += 6
        elif num == '0':
            sum += 6
    print(f'{sum} leds')

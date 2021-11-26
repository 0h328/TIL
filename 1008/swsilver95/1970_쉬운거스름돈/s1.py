import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# 50000 10000 5000 1000 500 100 50 10
for tc in range(1, T + 1):
    money = [0] * 8
    number = int(input())
    print('#{}'.format(tc))

    while number > 0:
        if number >= 50000:
            number -= 50000
            money[0] += 1
        if 10000 <= number < 50000:
            number -= 10000
            money[1] += 1
        if 5000 <= number < 10000:
            number -= 5000
            money[2] += 1
        if 1000 <= number < 5000:
            number -= 1000
            money[3] += 1
        if 500 <= number < 1000:
            number -= 500
            money[4] += 1
        if 100 <= number < 500:
            number -= 100
            money[5] += 1
        if 50 <= number < 100:
            number -= 50
            money[6] += 1
        if 10 <= number < 50:
            number -= 10
            money[7] += 1
        if number < 10:
            number = 0
    
    print(' '.join(map(str, money)))
import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, hexa = input().split()
    Conversion = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                  'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    result = ''
    temp = []

    for i in hexa[::-1]:
        temp.append(Conversion[i])

    for num in temp:
        for _ in range(4):
            result = str(num % 2) + result
            num //= 2
    print('#{} {}'.format(tc, result))


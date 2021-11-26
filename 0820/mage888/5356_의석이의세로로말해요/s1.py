import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    a = [input() for _ in range(5)]
    print(a)

    length_a = []
    for i in range(len(a)):
        length_a.append(len(a[i]))

    max_value = length_a[0]
    for i in length_a:
        if max_value < i:
            max_value = i

    result = ''
    for i in range(max_value):
        for j in range(len(a)):
            try:
                result += a[j][i]
            except:
                pass

    print('#{} {}'.format(tc, result))





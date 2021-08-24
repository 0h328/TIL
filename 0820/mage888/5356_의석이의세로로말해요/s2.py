import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    a = [''.join(input().split()) for _ in range(5)]

    for i in range(len(a)):
        max_value = len(a[i])
        for j in a:
            if max_value < len(j):
                max_value = len(j)

    result = ''
    for i in range(max_value):
        for j in range(len(a)):
            try:
                result += a[j][i]
            except:
                pass

    print('#{} {}'.format(tc, result))
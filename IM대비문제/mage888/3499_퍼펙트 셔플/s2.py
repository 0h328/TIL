import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = input().split()

    mid = N // 2
    left = data[:mid]
    right = data[mid:]
    res = []

    if N % 2:
        left = data[:mid+1]
        right = data[mid+1:]

    for i in range(len(right)):
        res.append(left[i])
        res.append(right[i])

    if N % 2:
        res.append(left[-1])

    print('#{} {}'.format(tc, ' '.join(res)))


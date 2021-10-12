import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input()) # 돈
    changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    print('#{}'.format(t))
    for change in changes:
        print(N // change, end=' ')
        if N // change:
            N %= change
    print()

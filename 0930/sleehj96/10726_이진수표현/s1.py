import sys
sys.stdin = open('input.txt')


for tc in range(int(input())):
    N, M = map(int, input().split())

    ans = 'ON'

    for j in range(N):
        if not M & (1 << j):
            ans = 'OFF'
            break

    print('#{} {}'.format(tc + 1, ans))
    # break

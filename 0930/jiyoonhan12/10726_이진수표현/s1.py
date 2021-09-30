import sys
sys.stdin = open('input.txt')

# 나눗셈 풀이

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    ans = 'ON'

    for i in range(N):
        if not M % 2:
            ans = 'OFF'
            break
        M //= 2

    print('#{} {}'.format(t, ans))
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cnt = 0
    while N != M:
        if M%2:
            M -= 1
            cnt += 1
        M //= 2
        cnt += 1
        if (M+1) == M:
            M += 1
            cnt += 1
            break
        if (M-1) == N:
            M -= 1
            cnt += 1
            break
    print(cnt)

2 7

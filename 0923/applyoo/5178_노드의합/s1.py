import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    t = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        t[a] = b

    for i in range(N, 0, -1):
        if t[i] == 0:
            if (i*2+1) <= N:
                t[i] += t[i*2] + t[i*2+1]
            else:
                t[i] += t[i*2]

        if i == L:
            print('#{0} {1}'.format(tc, t[i]))
            break

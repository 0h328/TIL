import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = input().split()
    s = [[] for _ in range(N)]

    n = 0
    for i in range(N):
        if N % 2:
            if i <= N//2:
                s[2*i].append(data[i])
            else:
                s[2*n+1].append(data[i])
                n += 1
        else:
            if i < N//2:
                s[2*i].append(data[i])
            else:
                s[2*n+1].append(data[i])
                n += 1

    print('#{}'.format(tc), end=' ')
    for i in range(N):
        print(*s[i], end=' ')
    print()


import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    M = int(input())
    p = [input() for _ in range(8)]
    N = len(p)

    r = c = 0

    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if p[i][j+k] != p[i][j+M-1-k]:
                    break
            else:
                r += 1

            for k in range(M//2):
                if p[j+k][i] != p[j+M-1-k][i]:
                    break
            else:
                c += 1

    print('#{} {}'.format(tc, r+c))
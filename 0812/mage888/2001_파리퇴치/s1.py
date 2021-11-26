import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = list(map(int,input().split()))
    a = [list(map(int,input().split())) for _ in range(n)]

    max_value = 0
    for i in range(n-m+1):
        for j in range(n-m+1):

            ans = 0

            for k in range(m):
                for l in range(m):
                    ans += a[i+k][j+l]

            if max_value < ans:
                max_value = ans

    print('#{} {}'.format(tc, max_value))
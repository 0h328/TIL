import sys

sys.stdin = open('input.txt')

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    list1 = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for j in range(N - M + 1):
        for k in range(N - M + 1):
            x = y = 0
            max_temp = 0
            while x < M:
                y = 0
                while y < M:
                    max_temp += list1[j + x][k + y]
                    y += 1
                x += 1
            if j == 0 and k == 0:
                ans = max_temp
            else:
                if ans < max_temp:
                    ans = max_temp
    print('#{} {}'.format(i + 1, ans))

# 함수로 구현
# 상하좌우 절대값 차이를 전부 더한 것
import sys
sys.stdin = open('input2.txt')

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_val = 0
    for r in range(N):
        for c in range(N):
            for k in range(4):
                nr = r+dr[k]
                nc = c+dc[k]
                if 0<=nr<N and 0<=nc<N:
                    sum_val+=abs(arr[nr][nc] - arr[r][c])

    print('#{} {}'.format((T+1), sum_val))

#1 2430
#2 2244
#3 0
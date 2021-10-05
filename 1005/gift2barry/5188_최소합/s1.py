# 총 소요시간 49분 21초

# thought process: 12분 12초
# dfs 활용하여 모든 경로에 대한 합 확인
# 가장 낮은 경로의 합을 지속적으로 갱신 후, 출력

# implement process:
# 주어진 2차원 배열에서 델타값으로 우측 & 아래 순서로 원소로 이동
# 이전 위치는 이동 대상 x, 고로 visited 필요 x
# 해당 원소에 도착 할 때마다 원소값 더해주고,
# 재귀에서 빠져나가면 원소값 다시 빼주기 반복

import time
import sys
sys.stdin = open('input.txt')

# start = time.time()

#    우  하
dr = (0, 1)
dc = (1, 0)

def dfs(r, c, k):
    global tmp
    global ans

    tmp += arr[r][c]

    if k == (N*2-2):    # 이 범위를 어떻게 하면 될까
        if tmp < ans:
            ans = tmp
        return

    # 현재 숫자 + 남은 이동 횟수 * 최소원소가 ans보다 크다면, 아래 내용 확인x
    if tmp + (((N*2-2) - k) * 1) > ans:
        return
    else:
        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                dfs(nr, nc, k+1)
                tmp -= arr[nr][nc]


for tc in range(1, int(input())+1):

    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    tmp = 0
    ans = 10000000000
    dfs(0, 0, 0)        # 행값, 열값, 깊이값
    print('#{} {}'.format(tc, ans))

# end = time.time()
# print('time taken: {} sec'.format(end - start))
# runtimeerror가 난다 17개 맞다고 함
# 이젠 그냥 오답이라고 함 53개 맞았다고 함 열받는당 히히

import sys
sys.stdin = open('input.txt')

def dfs(v, cnt):
    global result
    if cnt <= result:            # 계산한 값이 이전 값보다 크면
        return                   # 그냥 리턴해버림

    if v == N:        # v가 company의 길이와 같으면(넘어섰다는 뜻) 체크해볼건데
        if result < cnt:         # 현재 가지고 있는 값(result)보다 cnt 값이 작으면
            result = cnt         # result에 cnt 값을 넣어줄 것임(가장 작은 수 찾기라서)
        return

    for i in range(N):           # 반복문은 N번만큼 돌릴 것
        if i not in visited:     # 방문 체크하는 visited에 i값이 들어있지 않을 때만
            visited.append(i)    # visited에 i값을 넣어줄 것임
            dfs(v+1, cnt*percent[v][i]/100)             # 반복을 위해 dfs에 v+1을 넣어줌(제품1 체크 후 제품2...)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    result = 0
    cnt = 1
    dfs(0, 1)

    print('#{} {:.6f}'.format(tc, result*100))
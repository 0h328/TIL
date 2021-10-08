import sys
sys.stdin = open('input.txt')


def dfs(i, total):  # 행(직원), 성공확률을 인자로 넣음
    global ans
    if total <= ans:    # 기존값보다 작으면
        return          # 저장 안함
    if i == N:        # 기존값보다 크면
        ans = total     # ans에 저장

    for j in range(N):      # 열(작업) 체크
        if not visited[j]:  # 담당 안한 작업이라면
            visited[j] = 1  # 담당 체크
            dfs(i+1, total * p[i][j]/100)     # 수행하고 다음 직원으로 이동
            visited[j] = 0  # 다시 돌아가서 다른 경우 체크


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    ans = 0
    dfs(0, 1)
    print('#{} {:.6f}'.format(tc, ans*100))

import sys
sys.stdin = open('input.txt')


def dfs(i, total):  # 행, 총 생산비용을 인자로 넣음
    global ans
    if total >= ans:    # 기존값보다 크면
        return          # 저장 안함
    elif i == N:        # 기존값보다 작으면
        ans = total     # ans에 저장

    for j in range(N):      # 열 체크
        if not visited[j]:  # 생산 안한 공장이라면 (=방문 안한 열이라면)
            visited[j] = 1  # 방문체크
            dfs(i+1, total + fac[i][j])     # 생산하고 다음 제품(행)으로 이동
            visited[j] = 0  # 다시 돌아가서 다른 경우 체크


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    fac = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]     # 방문한 열인지만 체크
    ans = 9999999
    dfs(0, 0)
    print('#{} {}'.format(tc, ans))

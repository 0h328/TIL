# 문제 풀이 시간 : 30분
# 백트래킹 이용하는 문제였음 -> dfs 사용해야함 (다 돌면서 최소값 찾아야해서)
# 솔직히 전기버스2랑 비슷해서 좀 덜 걸린듯 하다.
# visited 생각을 못해서 계속 고민했다.

import sys
sys.stdin = open('input.txt')

def dfs(v):
    global cnt, result
    if cnt >= result:             # 계산한 값이 이전 값보다 크면
        return                    # 그냥 리턴해버림

    if v == len(company):         # v가 company의 길이와 같으면(넘어섰다는 뜻) 체크해볼건데
        result = cnt          # result에 cnt 값을 넣어줄 것임(가장 작은 수 찾기라서)
        return

    for i in range(N):            # 반복문은 N번만큼 돌릴 것
        if i not in visited:      # 방문 체크하는 visited에 i값이 들어있지 않을 때만
            visited.append(i)     # visited에 i값을 넣어줄 것임
            cnt += company[v][i]  # 넣고 그 위치에 해당하는 값을 cnt에 더해줄 것임
            dfs(v+1)              # 반복을 위해 dfs에 v+1을 넣어줌(제품1 체크 후 제품2...)
            visited.pop()         # 확인 끝나고 나오면 visited에서 마지막 값을 빼줌
            cnt -= company[v][i]  # cnt에 값을 빼준다. -> 왜냐면 백트래킹이니까~~~ ♪

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    company = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    result = 2000                 # 최대 한 1500 정도 되는 것 같아서 넉넉잡아 2000으로 설정
    cnt = 0
    dfs(0)                        # 제품1부터 시작하기 위해서
    print('#{} {}'.format(tc, result))

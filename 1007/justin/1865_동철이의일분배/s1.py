def dfs(k, total):
    global ans
    if total <= ans:                           # 가지치기
        return
    if N == k:                                 # 모든 사람의 성공 확률을 다 확인 했으면
        ans = max(total, ans)                  # 최댓값 갱신
        return
    for i in range(N):
        if not things[i]:                      # 아직 확인 안한 일이 있다면
            things[i] = 1                      # 그 일을 확인했다는 체크를 하고
            dfs(k+1, total*data[k][i] / 100)   # k번째 사람의 i번째 성공 확률을 합하고 다음 사람(k+1) 확인
            things[i] = 0                      # 확인 이후 이전 단계로 가기 위해 원복

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T):
    ans = 0                                                     # 최댓값 누적
    things = [0 for _ in range(16)]                             # N명의 직원이 N개의 일 (0 ~ 15 총 16)
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]  # N*N
    dfs(0, 100)                                                 # k번째 사람
    print('#{} {:.6f}'.format(tc, ans))
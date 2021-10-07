def solve(perm_idx, prev_idx, usage):     # perm_idx은 순열의 인덱스, prev_idx는 이전 위치, usage는 소비량
    global ans
    if perm_idx == N:                     # 순열이 완성된 경우
        usage += data[prev_idx][0]        # 사무실까지의 거리 추가 (사무실은 1번으로 고정)
        # ans = min(ans, usage)
        if ans > usage:                   # 기존의 최소값보다 작으면 최솟값 갱신
            ans = usage
    elif ans <= usage:                    # 가지치기 -> 순열이 완성되지 않았지만 합이 최소값보다 큰 경우
        return
    else:
        for i in range(1, N):                                  # 순열의 perm_idx번 인덱스에 들어갈 숫자 선택
            if not visited[i]:
                visited[i] = 1                                 # 방문 체크
                solve(perm_idx+1, i, usage+data[prev_idx][i])  # 다음 확인
                visited[i] = 0                                 # 원상 복구

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N+1)]                           # 사용한 숫자 표시
    ans = 987654321
    visited[0] = 1                                              # 0번은 사무실이므로 고정
    solve(1, 0, 0)
    print('#{} {}'.format(tc, ans))
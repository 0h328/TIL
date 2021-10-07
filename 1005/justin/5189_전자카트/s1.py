def solve(k, cost):                      # k: 출발 / cost: 배터리 사용량
    global ans
    if cost >= ans:                      # 최소 비용에 대한 가지치기
        return
    if k == N:                           # 구역을 다 돌아봤으면
        cost += data[order[N-1]][0]      # 마지막에 방문한 번호(N-1)에서 [0]으로 가는 배터리 사용량 누적 (사무실의 위치는 고정)
        ans = min(ans, cost)             # 최솟값 갱신
    else:
        for i in range(k, N):                                       # 1번(사무실 다음부터) 하나씩 체크하며
            order[k], order[i] = order[i], order[k]                 # 교환해보자
            # 다음 단계로 넘겨주는 배터리 사용량
            # cost(지금까지의 배터리 총 사용량) + order[k-1]에서 order[k]로 가는데 들어가는 배터리 사용량
            solve(k+1, cost+data[order[k-1]][order[k]])             # 다음 구역 확인
            order[k], order[i] = order[i], order[k]                 # 원상 복구

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())                                              # 구역의 수
    data = [list(map(int, input().split())) for _ in range(N)]    # 인접 행렬
    order = [i for i in range(N)]                                 # 방문 순서(0번(사무실) / 1번 ~ N-1번(관리구역) -> 구역 번호를 의미(반드시 한 번씩만 방문)
    ans = 987654321
    solve(1, 0)                                                   # 첫 번째 인자: 출발 지점(0번은 사무실이기 때문에 1번 ~ N-1까지의 순열 정보만 있으면 됨) & 두 번째 인자: 배터리 사용량
    print('#{} {}'.format(tc, ans))
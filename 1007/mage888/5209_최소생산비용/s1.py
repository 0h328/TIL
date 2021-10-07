import sys
sys.stdin = open('input.txt')

def dfs(product):
    global min_num, cost

    if min_num < cost:  # 전체 비용보다 제품 한개의 비용보다 작은 경우는 종료
        return

    for i in range(N):
        if not visited[i]:                      # 방문하지 않은 공장
            visited[i] = 1                      # 공장 방문 체크
            cost += arr[product][i]             # 비용에 누적
            dfs(product+1)                      # 다음 제품 체크하러
            cost -= arr[product][i]             # 다른 비용 찾기 위해 백트래킹
            visited[i] = 0                      # 방문지도 back

    if product == N:                            # 제품을 모두 확인한 경우
        if cost < min_num:
            min_num = cost                      # 최소 비용 갱신

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]   # product * factory

    visited = [0] * N   # 제품당 공장이 겹치면 안되므로, 열의 개수만큼 생성
    min_num, cost = 100*N, 0

    dfs(0)  # 첫번째 제품부터 시작

    print('#{} {}'.format(tc, min_num))


#1-1. 시간 초과

# def dfs(r, c, dist):                              # 현재 위치 (행/열) / dist: 누적 거리
#     global ans
#     if r == N-1 and c == N-1:                     # 도착지점에 도착한 경우
#         ans = min(ans, dist)                      # ans에 지금까지 최소거리 갱신
#     else:                                         # 도착하지 않았다면
#         if r + 1 < N:                             # 아래로 이동 했을 때 범위를 벗어나지 않으면
#             dfs(r+1, c, dist + arr[r+1][c])       # 아래로 이동 (값 누적)
#         if c + 1 < N:                             # 오른쪽으로 이동 했을 때 범위를 벗어나지 않으면
#             dfs(r, c+1, dist + arr[r][c+1])       # 오른쪽으로 이동 (값 누적)
#
# import sys
# sys.stdin = open('input.txt')
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = 987654321
#     dfs(0, 0, arr[0][0])                          # 0, 0에서 시작 / 누적거리 초기값 -> arr[0][0]
#     print('#{} {}'.format(tc, ans))


#1-2. 시간 초과 해결
def dfs(r, c, dist):                          # 현재 위치 (행/열) / dist: 누적 거리
    global ans
    if dist >= ans:                           # 가지치기
        return                                # 만약 지금 계산 중인 거리(dist)가 지금까지의 최솟값(ans)보다 크거나 같으면 볼 필요가 없음

    if r == N-1 and c == N-1:                 # 도착지점에 도착한 경우
        ans = min(ans, dist)                  # ans에 지금까지 최소거리 저장
    else:                                     # 도착하지 않았다면
        if r + 1 < N:                         # 아래로 이동 했을 때 범위를 벗어나지 않으면
            dfs(r+1, c, dist + arr[r+1][c])   # 아래(row+1)로 이동 (거리 누적)
        if c + 1 < N:                         # 오른쪽으로 이동 했을 때 범위를 벗어나지 않으면
            dfs(r, c+1, dist + arr[r][c+1])   # 오른쪽(col+1)으로 이동 (거리 누적)

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]  # N * N 판
    ans = 987654321                                            # 최솟값 초기화
    dfs(0, 0, arr[0][0])                                       # 0, 0에서 시작 / 누적거리 초기값 -> arr[0][0]
    print('#{} {}'.format(tc, ans))
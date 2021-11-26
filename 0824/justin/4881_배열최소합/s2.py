def calc_min(cur_sum):          # 최솟값 갱신
    global ans
    if ans > cur_sum:
        ans = cur_sum
    return

def solve(k, cur_sum):
    global ans
    if ans <= cur_sum:
        return
    if N == k:                  # k가 N이 된다? -> 다 봤으면는 것은 마지막 row(N)에 도착했다는 의미
        calc_min(cur_sum)       # 최솟값 갱신 여부 결정
    else:                       # 아직 모든 row/col을 안봤다면
        for idx in range(k, N): # k부터 N-1까지 돌면서
            visited[k], visited[idx] = visited[idx], visited[k]
            # cursum + data[k][visited[k]] -> 현재 합에 새로운 열의 숫자를 합산 (visited[k] -> 열을 결정)
            # k+1 -> 다음 행을 확인
            solve(k+1, cur_sum + data[k][visited[k]])
            visited[k], visited[idx] = visited[idx], visited[k]

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    ans = 987654321       # 최솟값을 구하기 위한 임의의 최댓값 설정
    N = int(input())      # 행렬 크기
    visited = [0] * N     # arr -> [0, 1, 2] -> 열의 값을 미리 조정
    for i in range(N):
        visited[i] = i
    data = [list(map(int, input().split())) for _ in range (N)]
    solve(0, 0)           # k(index), cur_sum(현재까지의 누적합)
    print('#{} {}'.format(tc, ans))
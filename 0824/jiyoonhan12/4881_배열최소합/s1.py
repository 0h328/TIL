import sys
sys.stdin = open('input.txt')

def solve(i):
    global total, mini

    if total > mini: # 현재 합이 최소값보다 크면 볼 필요 없음
        return

    if i == N: # N개 다 채웠는데 합이 최소값보다 작으면 최소값 갱신 후 함수 끝냄
        if total < mini:
            mini = total
            return

    for j in range(N): # 열을 기준으로 안 고른 거 집어넣기
        if not visited[j]:
            visited[j] = 1
            total += arr[i][j]
            solve(i+1) # 다음 행까지 보고
            total -= arr[i][j] # 함수 끝났으면 원상복구
            visited[j] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N # 열 방문
    total, mini = 0, 9**2 # 최대값 9로 채워진 9*9배열... 사실 아무거나 큰 수면 상관없음
    solve(0)
    print('#{} {}'.format(t, mini))

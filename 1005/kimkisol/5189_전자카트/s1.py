import sys

sys.stdin = open('input.txt')


def dfs(nr, temp_sum, cnt):
    global min_sum

    if temp_sum > min_sum:
        return
    if cnt == N - 1:
        temp_sum += nums[nr][0]  # POINT) 1이 아니라 0이다 헷갈림 ㅠ
        if temp_sum < min_sum:
            min_sum = temp_sum
        return

    for i in range(1, N):
        if not visited[i]:
            visited[i] = 1
            dfs(i, temp_sum + nums[nr][i], cnt + 1)
            visited[i] = 0  # POINT) visited 해제!


T = int(input())

for t in range(1, T + 1):
    N = int(input())  # N: 가로 세로 줄
    nums = [list(map(int, input().split())) for _ in range(N)]  # 2차원 숫자 배열
    visited = [1] + [0] * (N - 1)  # 2번째~마지막번째 관리구역
    min_sum = 100 * (N + 1)  # 100이하의 자연수 최대 N개 선택

    dfs(0, 0, 0)

    print('#{} {}'.format(t, min_sum))

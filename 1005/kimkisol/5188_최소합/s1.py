import sys

sys.stdin = open('input.txt')


def dfs(p, temp_sum):
    global min_sum

    if temp_sum > min_sum:
        return
    if p == end:
        if temp_sum < min_sum:
            min_sum = temp_sum
            return

    for i in range(2):
        nr, nc = p[0] + dr[i], p[1] + dc[i]
        if nr < N and nc < N:
            dfs((nr, nc), temp_sum + nums[nr][nc])


T = int(input())

for t in range(1, T + 1):
    N = int(input())  # N: 가로, 세로 칸 수
    nums = [list(map(int, input().split())) for _ in range(N)]  # 2차원 숫자 배열
    dr = [1, 0]  # 아래, 오른쪽
    dc = [0, 1]
    end = (N - 1, N - 1)  # 끝점: (마지막인덱스, 마지막인덱스)
    min_sum = 20 * N  # 최대 자연수 10 * (N * 2 - 1)인데 그냥 20 * N으로 씀

    dfs((0, 0), nums[0][0])

    print('#{} {}'.format(t, min_sum))

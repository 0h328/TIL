import sys
# 330ms
sys.stdin = open('input.txt')
'''
POINT) 이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 됨 (visited가 필요없음)
'''


def dfs(length, r, c, num):
    if length == 7:
        nums.add(num)
        return
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(length + 1, nr, nc, num + arr[nr][nc])


T = int(input())

for t in range(1, T + 1):
    arr = [input().split() for _ in range(4)]
    dr = [0, 1, 0, -1]  # 우하좌상
    dc = [1, 0, -1, 0]
    nums = set()

    for i in range(4):
        for j in range(4):
            dfs(1, i, j, arr[i][j])

    print('#{} {}'.format(t, len(nums)))

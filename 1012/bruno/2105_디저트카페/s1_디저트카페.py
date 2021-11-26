import sys
sys.stdin = open('input.txt')


def solve(row, col, dir):
    global result
    if dir == 3 and (row == starti and col == startj):
        if len(dessert_list) > result:
            result = len(dessert_list)

    nr = row + dr[dir % 4]
    nc = col + dc[dir % 4]

    if 0 <= nr < n and 0 <= nc < n:
        if dessert[nr][nc] not in dessert_list:
            dessert_list.append(dessert[nr][nc])
            solve(nr, nc, dir)
    dir += 1
    nr = row + dr[dir % 4]
    nc = col + dc[dir % 4]

    if 0 <= nr < n and 0 <= nc < n:
        if dessert[nr][nc] not in dessert_list:
            dessert_list.append(dessert[nr][nc])
            solve(nr, nc, dir)

    if dessert_list:
        dessert_list.pop()

for tc in range(1, int(input())+1):
    n = int(input())
    dessert = [list(map(int, input().split())) for _ in range(n)]
    dr = [-1, 1, 1, -1]
    dc = [1, 1, -1, -1]
    result = -1
    for i in range(1, n-1):
        for j in range(n-2):
            dessert_list = []
            starti, startj = i, j
            solve(i, j, 0)
    print('#{} {}'.format(tc, result))
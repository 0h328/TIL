import sys
sys.stdin = open('input.txt')


def solve(row, col, dir):
    global result
    if dir == 2:
        if len(dessert_list) * 2 <= result:
            return

    if dir == 3 and (row == starti and col == startj):
        if len(dessert_list) > result:
            result = len(dessert_list)

    nrow = row + drow[dir % 4]
    ncol = col + dcol[dir % 4]

    if 0 <= nrow < n and 0 <= ncol < n:
        if dessert[nrow][ncol] not in dessert_list:
            dessert_list.append(dessert[nrow][ncol])
            solve(nrow, ncol, dir) # 계속 같은 방향으로 진행 시켜주고
            solve(nrow, ncol, dir + 1) # 방향 전환
            if dessert_list:
                dessert_list.pop()


for tc in range(int(input())):
    n = int(input())
    dessert = [list(map(int, input().split())) for _ in range(n)]
    drow = [-1, 1, 1, -1] # 오위, 오아, 왼아, 왼위
    dcol = [1, 1, -1, -1]
    result = -1
    for i in range(1, n-1):
        for j in range(n-2):
            dessert_list = []
            starti, startj = i, j # 시작 값을 비교하기 위해서
            solve(i, j, 0)
    print('#{} {}'.format(tc+1, result))
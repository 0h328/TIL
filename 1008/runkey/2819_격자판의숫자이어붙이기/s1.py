import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, temp):
    global result

    if len(temp) == 7:
        result.add(temp)
        return

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, temp + str(n_list[nr][nc]))

tc = int(input())
for t in range(1, tc + 1):
    result = set()
    n_list = [list(map(int, input().split())) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            temp = str(n_list[i][j])
            dfs(i, j, temp)
    print("#{} {}".format(t, len(result)))
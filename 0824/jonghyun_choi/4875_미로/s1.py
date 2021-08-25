import sys
sys.stdin = open('input.txt')

T = int(input())

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def dfs(i,j):
    global res
    for k in range(4):
        new_dr = i + dr[k]
        new_dc = j + dc[k]
        if 0 <= new_dr < N and 0 <= new_dc < N and data[new_dr][new_dc] != '1':
            if data[new_dr][new_dc] == '3':
                res = 1
                break
            else:
                data[new_dr][new_dc] = '1'
                dfs(new_dr, new_dc)

    return res


for case in range(T):
    N = int(input())
    data = [list(input()) for _ in range(N)]
    res = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '2':
                print('#{} {}'.format(case + 1, dfs(i, j)))

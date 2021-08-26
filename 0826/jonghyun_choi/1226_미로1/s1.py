import sys
sys.stdin = open('input.txt')

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def BFS(i, j):
    global res
    q = []
    q.append((i,j))
    while q:
        r, c = q.pop(0)
        for k in range(4):
            next_r = r + dr[k]
            next_c = c + dc[k]
            if 0 <= next_r < 16 and 0 <= next_c < 16 and data[next_r][next_c] != '1':
                if data[next_r][next_c] == '3':
                    res = 1
                    break
                else:
                    data[next_r][next_c] = '1'
                    q.append((next_r,next_c))

for _ in range(10):
    N = int(input())
    data = [list(map(str,input())) for _ in range(16)]
    res = 0
    for i in range(16):
        for j in range(16):
            if data[i][j] == '2':
                BFS(i, j)

    print('#{} {}'.format(N, res))
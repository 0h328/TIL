import sys
sys.stdin = open('input.txt')

dr = [0,0,-1,1]
dc = [1,-1,0,0]

def find_sol(r, c, ans, cnt):
    if cnt == 7:
        result.add(ans)
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < 4 and 0<= nc < 4:
            find_sol(nr, nc, ans+matrix[nr][nc], cnt+1)

for T in range(int(input())):
    result = set()
    matrix = [input().split() for _ in range(4)]
    for i in range(4):
        for j in range(4):
            find_sol(i, j, matrix[i][j], 1)
    
    print('#{} {}'.format((T+1), result))

#1 23

import sys
sys.stdin = open("input.txt")
direct = [
    [-1, 1],
    [1, 1],
    [1, -1],
    [-1, -1],
]

def dfs(a, b, check, idx):
    global result
    if board[a][b] not in check:
        check.append(board[a][b])
        
        for k in range(idx, 4):     # 방향
            dx, dy = a+direct[k][0], b+direct[k][1]
            
            if dx in range(N) and dy in range(N):
                if dx == start_i and dy == start_j:
                    if len(check) >= 4:
                        if result < len(check):
                            result = len(check)
                            check.pop()
                            return
                dfs(dx,dy, check, idx)

T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = -9999999

    for i in range(N):
        for j in range(N):
            check = []
            start_i = i
            start_j = j

            dfs(i, j, check, 0)
    print("#{} {}".format(t+1, result))
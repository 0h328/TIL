import sys
import time
from collections import deque
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt')


def dfs(y, x, k, move, num):
    global visited

    if not move:
        return

    print(f'----- 벽돌 -----')
    for a in range(H):
        for b in range(W):
            print(board[a][b], end=' ')
        print()

    print(f'----- 방문 -----')
    for a in range(H):
        for b in range(W):
            print(visited[a][b], end=' ')
        print()
    time.sleep(0.5)

    r = y + dr[k]
    c = x + dc[k]

    if 0 <= r < H and 0 <= c < W:       # 범위 내
        if visited[r][c] == num:                        # 같은 폭탄에 터진거라면, 그냥 진행
            dfs(r, c, k, move-1, num)
        
        elif visited[r][c]:                             # 다른 폭탄에 터진거라면, 그 위로 올라감 (위에꺼가 내려왔을거기 때문)
            for i in range(r, -1, -1):
                if not visited[i][c] and board[i][c] > 1:   # 그 위 벽돌이 값이 1보다 크면 4방향으로 추가 터짐
                    visited[i][c] = num
                    dfs(r, c, k, move-1, num)
                    for q in range(4):
                        dfs(r, c, q, board[i][c]-1, num)
                    break
                elif not visited[i][c] and board[i][c] == 1:        # 그 위 벽돌이 1이면 한번 터지고 끝
                    dfs(r, c, k, move-1, num)
            else:                                       # 그 위 값이 0이면 그냥 진행
                dfs(r, c, k, move-1, num)

        elif not visited[r][c] and board[r][c] > 1:     # 이전에 터지지 않았고, 벽돌이 1보다 크면 (추가로 터지게 되면)
            visited[r][c] = num
            dfs(r, c, k, move-1, num)                   # 기존에 터지던건 계속 터짐
            for q in range(4):                          # 새로 큰 벽돌이므로 그 범위만큼 추가로 터짐 (4방향)
                dfs(r, c, q, board[r][c]-1, num)
        
        elif not visited[r][c] and not board[r][c]:     # 이전에 터지지 않았고, 벽돌이 아니면 그냥 진행
            dfs(r, c, k, move-1, num)
        
        elif not visited[r][c] and board[r][c] == 1:
            visited[r][c] = num
            dfs(r, c, k, move-1, num)
        



def solution(arr):              # 벽돌이 떨어지는 가로의 인덱스 값을 배열로 받으면 실행
    global visited

    visited = [[0] * W for _ in range(H)]

    num = 0
    for e in arr:
        print(e)
        num += 1
        for i in range(H):
            if board[i][e] and not visited[i][e]:
                visited[i][e] = num
                print(i, e, board[i][e]-1, num)
                for k in range(4):
                    dfs(i, e, k, board[i][e]-1, num)
                
                break


def case(idx, arr):             # 벽돌이 떨어지는 경우들을 구해줌
    if idx >= N:
        solution([2])
        return

    for j in range(W):
        arr.append(j)
        case(idx+1, arr)
        arr.pop()


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())     # 구슬 떨어뜨리는 횟수 / 가로 / 세로
    board = [list(map(int, input().split())) for _ in range(H)]
    visited = []
    
    # case(0, [])
    solution([2, 2, 7])
    print('end')

import sys
sys.stdin = open('input.txt')

# DFS
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c, board):
    global max_cnt
    max_cnt = max(max_cnt, len(board))

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < R and 0 <= nc < C:
            if arr[nr][nc] not in board:    # 이동할 위치에 누적될 알파벳이 없을 조건
                board += arr[nr][nc]        # 알파벳을 누적해서 더하기
                dfs(nr, nc, board)          # dfs탐색
                board = board[:-1]          # 나오면 이전에 더한 알파벳 빼기(백트래킹)

R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for _ in range(R)]
max_cnt = 0

dfs(0, 0, arr[0][0])    # (행, 열, 시작알파벳)
print(max_cnt)

# BFS
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]
#
# def bfs(x, y):
#     global res
#
#     # set 사용 이유 : 시간복잡도 O(1) / deque는 O(N)
#     q = {(x, y, arr[x][y])}
#
#     while q:
#         r, c, board = q.pop()
#
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#
#             if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] not in board:
#                 q.add((nr, nc, board+arr[nr][nc]))
#                 res = max(res, len(board) + 1)
#
# R, C = map(int, sys.stdin.readline().split())
# arr = [list(sys.stdin.readline()) for _ in range(R)]
# res = 1
#
# bfs(0, 0)
# print(res)
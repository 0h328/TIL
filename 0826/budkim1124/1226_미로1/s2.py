def bfs(start_i, start_j):
    global result

    Q = []
    Q.append((start_i, start_j))

    if arr[start_i][start_j] == '3':
        result = 1
        return
    for





import sys
sys.stdin = open("input.txt")

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(10):
    N = int(input())
    arr = [list(input()) for _ in range(16)]
    # print(arr)
    visited = []

    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                start_i, start_j = i, j

    result = 0
    bfs(start_i, start_j)
    print("#{} {}".format(N, result))
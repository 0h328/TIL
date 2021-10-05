import sys
sys.stdin = open('input.txt')
'''
def bfs(start, end):
    global result
    if start == t-1 and end == t-1:
        return
    que = deque()
    que.append((start, end))
    while que:
        start, end = que.popleft()
        for i in range(4):
            nrow = start + drow[i]
            ncol = end + dcol[i]
            if 0 <= nrow < t and 0 <= ncol < t and visited[nrow][ncol] == 0:
                visited[nrow][ncol] = visited[start][end] + num[start][end]
                que.append((nrow, ncol))
'''
def dfs(start, end):
    global result_min
    if result_min < visited[start][end]: # 현재 더하고 있는 방문의 값이 첫번째 result보다 큰 경우 중단
        return

    if start == t-1 and end == t-1: # t,t 에 도착하는 경우 result 갱신
        if result_min > visited[start][end]:
            result_min = visited[start][end]
            return

    for i in range(2):
        nrow = start + drow[i]
        ncol = end + dcol[i]
        if 0 <= nrow < t and 0 <= ncol < t and visited[nrow][ncol] == 0:
            visited[nrow][ncol] = visited[start][end] + num[start][end]
            dfs(nrow, ncol)
            visited[nrow][ncol] = 0


for tc in range(int(input())):
    t = int(input())
    num = [list(map(int, input().split())) for _ in range(t)]
    visited = [[0] * t for _ in range(t)]
    drow = [0, 1]  # 오른쪽과 왼쪽 방문 x ★★★★★
    dcol = [1, 0]
    result_min = 1700
    dfs(0, 0)
    last_num = num[t-1][t-1]
    print('#{} {}'.format(tc+1, result_min+last_num))
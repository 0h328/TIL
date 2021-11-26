import sys
sys.stdin = open('input.txt')
#stack 사용, while stack 반복문으로 구현, visited에 방문 좌표 넣어주는 방법(재귀X)
def dfs(start, data):
    #1. 함수 시작하자 마자 visited 찍어주기
    stack = [start]
    visited = []
    while stack:#스택에 넣어줬으니까 시작 가능
        r, c = stack.pop()
        visited.append((r, c))
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            w = (nr, nc)
            if 0 <= nr < N and 0 <= nc < N:
                if data[nr][nc] == 3:
                    return 1
                if not data[nr][nc] and w not in visited:
                    stack.append(w)

    #다 돌았는데도 없으면! 갈 수 없다는 거임
    return 0

def find_start(data, N):
    for r in range(N):
        for c in range(N):
            if data[r][c] == 2:
                #튜플로 반환됨
                return r, c

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    start = find_start(data, N)

    ans = dfs(start, data)
    print('#{} {}'.format(tc, ans))

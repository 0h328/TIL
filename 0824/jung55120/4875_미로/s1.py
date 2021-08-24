# 문제 푼 시간 : 2시간
# 문제 생각 흐름 : stack을 써보는게 어떨까? -> 코드 리뷰 후 : 아하 dfs 쓰는게 좋겠어~ (하지만 뭔지 모르는게 함정)
# 혼자서 풀었는가 ? No, 코드 리뷰 듣고 흐름 파악 후 혼자 풀기 (+ 구글링)

import sys
sys.stdin = open('input.txt')

def find_miro(x, y):
    global result
    if miro[x][y] == 3: # 만약 x, y좌표가 3이면 result = 1
        result = 1
        return          # 끝내기

    miro[x][y] = 1      # miro[x][y]는 방문했기 때문에 1로 바꿔줌 -> 이러면 다시 체크할 필요 없음!

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and miro[nx][ny] != 1: # length 범위 안에 있고, 미로의 수가 1이 아닐 때
            find_miro(nx, ny) # 재귀를 이용해 다시 반복


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    result = 0

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2: # 2의 위치 찾기
                find_miro(i, j)


    print('#{} {}'.format(tc, result))
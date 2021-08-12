import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(100)]

    # 아무리 생각해도 위에서 목적지를 찾는 방법을 못찾겠음.
    # 그래서, 목적지로부터 출발지를 찾는 방법을 선택.

    r = 99 # 목적지는 무조건 99번째 행에 있으므로 고정
    c = ?  # 열이 어디 위치에 있는지 찾는 방법을 모르겠음.

    dr = [-1, 0, 0] # r은 위로 갈때 -1, 좌,우로 갈때는 0
    dc = [0, 1, -1] # c는 위로 갈때 0, 우로 갈때 1, 좌로 갈때 -1

    while r > 0: # r이 0이 되면 출발지를 찾았으므로 종료
        nr = r + dr[i] # nr은 r이 배열 내 dr만큼 이동한 곳
        nc = c + dc[i] # nc는 c가 배열 내 dc만큼 이동한 곳

        if nr in range(100) and nc in range(100): # 범위 벗어나는 것을 방지

import sys
sys.stdin = open('input.txt')
for _ in range(1, 11):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    for col_x in range(100):          # 출발점 -> 시작점
        if data[99][col_x] == 2:      # 도착지
            row, col = 99, col_x  # 그때의 좌표 저장

    # 방향 델타
    # 좌 우 상 -> 도착지부터 올라가기 때문에 아래는 볼 필요 없음
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    while row != 0:         # 가장 윗부분에 도달하면 끝
        for i in range(3):  # 방향 델타로 이동 (주위를 둘러보고 왼쪽이나 오른쪽으로 갈 길이 있으면 가자)
            nr = row + dr[i]
            nc = col + dc[i]
            if 0 <= nr < 100 and 0 <= nc < 100: # 범위 체크
                if data[nr][nc]:                # 현재 위치로부터 왼쪽/오른쪽/위쪽에 길이 있다면 (가야 할 곳으로 미리 탐색)
                    data[row][col] = 0          # 0으로 변경(다시 보지 않기 위함)
                    row += dr[i]                # 현재 위치 갱신 -> 움직여야 할 곳으로 이동
                    col += dc[i]
    print('#{} {}'.format(tc, col))
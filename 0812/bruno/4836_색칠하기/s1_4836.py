import sys
sys.stdin = open('input.txt')

T = int(input())
for num in range(1, T+1):
    base = [[0] * 10 for _ in range(10)]            # 0으로 된 흰 도화지 생성
    color_cnt = int(input())                        # 칠할 색 갯수

    for _ in range(color_cnt):
        paint = list(map(int, input().split()))     # 칠할 색 & 좌표 입력

        if paint[4] == 1:                               # 빨간색일 때
            for r in range(paint[0], paint[2]+1):       # 칠할 row 범위
                for c in range(paint[1], paint[3]+1):   # 칠할 column 범위
                    base[r][c] += 1                     # 해당 범위 1 증가

        if paint[4] == 2:                               # 파란색일 때
            for r in range(paint[0], paint[2]+1):       # 칠할 row 범위
                for c in range(paint[1], paint[3]+1):   # 칠할 column 범위
                    base[r][c] += 2                     # 해당 범위 2 증가

    cnt = 0                         # 보라색 칸 갯수
    for i in range(9):              # 전체 도화지 범위에서
        for j in range(9):
            if base[i][j] == 3:     # 값이 3이면(보라색이면)
                cnt += 1            # 갯수 증가
    print('#{} {}'.format(num, cnt))
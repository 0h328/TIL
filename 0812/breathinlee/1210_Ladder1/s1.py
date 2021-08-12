import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    T = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    end_point = data[99].index(2)  # 99행에서 도착점의 열
    col_direction = [0, -1, 1]   # 상좌우(아래에서 위로 가니까 하는 없어도 됨)
    row_direction = [-1, 0, 0]   # 상좌우
    row, col = 99, end_point   # 뒤에서부터 찾아갈 것
    d = 0   # 방향

    while row >= 0:
        if col >= 1 and data[row][col - 1] == 1:    # 왼쪽에 1 있으면 방향 바꿔줌
            d = 1
            while True:
                row += row_direction[d]
                col += col_direction[d]
                if col < 1 or data[row][col - 1] == 0:  # 왼쪽으로 쭉 가다가 0을 만나게 되면 정지
                    break
        elif col <= 98 and data[row][col + 1] == 1:  # 오른쪽에 1 있으면 방향 바꿔줌
            d = 2
            while True:
                row += row_direction[d]
                col += col_direction[d]
                if col > 98 or data[row][col + 1] == 0:  # 오른쪽으로 쭉 가다가 0을 만나게 되면 정지
                    break
        d = 0
        row += row_direction[d]
        col += col_direction[d]

    print('#{} {}'.format(tc, col))













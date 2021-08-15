import sys

sys.stdin = open('input.txt')

T = int(input())
N = 9
for_check = '123456789'

def sudoku_check(data):
    data_reverse = list(map(list, zip(*data)))
    # 가로, 세로 확인
    # data와 행, 열 변환한 reverse의 행을 하나씩 정렬하고 for_check와 같은지 확인
    for i in range(N):
        if ''.join(list(map(str, sorted(data[i])))) != for_check:
            return 0
        if ''.join(list(map(str, sorted(data_reverse[i])))) != for_check:
            return 0

    # 3x3 확인. 0~2/3~5/6~8을 left/center/right에 담고 row%3 == 2일 때마다 리스트 초기화
    left = []
    center = []
    right = []
    for row in range(N):
        for col in range(N):
            if col < 3:
                left.append(data[row][col])
            elif col < 6:
                center.append(data[row][col])
            else:
                right.append(data[row][col])

        if row % 3 == 2:
            if ''.join(list(map(str, sorted(left)))) != for_check:
                return 0
            if ''.join(list(map(str, sorted(center)))) != for_check:
                return 0
            if ''.join(list(map(str, sorted(right)))) != for_check:
                return 0
            left = []
            center = []
            right = []
    else:
        return 1

for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = sudoku_check(data)
    print('#{} {}'.format(tc, ans))



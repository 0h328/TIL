import sys
sys.stdin = open('input.txt')


def sdoku_column(arr, column):  # 2중 리스트에서 컬럼을 반환하는 함수
    result = []  # column번째 열의 값들을 저장할 공간

    for i in range(len(arr)):
        result.append(arr[i][column])

    return result


def sdoku_box(arr, box):  # 2중 리스트에서 박스를 반환하는 함수
    boxes = []  # box번째 박스의 값들을 저장할 공간
    value = box // 3

    for i in range(value + 3):
        for j in range(value + 3):
            boxes.append(arr[i][j])

    return boxes


def sdoku_verification(arr):
    for i in range(9):
        if len(set(arr[i])) != 9:  # 행 검사
            return 0

        if len(set(sdoku_column(arr, i))) != 9:  # 열 검사
            return 0

        if len(set(sdoku_box(arr, i))) != 9:  # 박스 검사
            return 0
    return 1


T = int(input())

for test in range(T):
    sdoku = []
    for i in range(9):
        sdoku.append(list(map(int, input().split())))
    print('#{} {}'.format(test+1, sdoku_verification(sdoku)))
import sys

sys.stdin = open('input.txt')


def check_straight(data): # visit한 거랑 비슷하다 넣어보고 만약 중복되면 그건 잘못된거다
    for i in range(9):
        check = []
        for j in range(9):
            if check:
                if data[i][j] in check:
                    return False
            check.append(data[i][j])
    return True


def check_block(data): # 가로 세로 시작점 설정해주고 거기서 3번씩만 돌리려고 하다보니 포문이 4개..... 줄일 수 있을까?
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = []
            for h in range(3):
                for k in range(3):
                    if check:
                        if data[i + h][j + k] in check:
                            return False
                    check.append(data[i + h][j + k])
    return True


for test in range(1, 1 + int(input())):

    data = [list(map(int, input().split())) for _ in range(9)]
    trans = [i for i in zip(*data)] # 전치행렬

    answer = check_straight(data) and check_straight(trans) and check_block(data) # 모두 트루일때만 트루인거다

    if answer:
        print('#{} {}'.format(test, 1))
    else:
        print('#{} {}'.format(test, 0))

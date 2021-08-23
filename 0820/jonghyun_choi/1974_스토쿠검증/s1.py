import sys
sys.stdin = open('input.txt')

T = int(input())

def check_sdoku(data):
    for i in range(len(data)):
        check = []
        for j in range(len(data[i])):
            if data[i][j] not in check:
                check.append(data[i][j])
        if len(check) != 9:
            return False
    else:
        return True

def grid_check(data):
    for i in range(0, len(data), 3):
        for j in range(0, len(data), 3):
            check = []
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    if data[k][l] not in check:
                        check.append(data[k][l])
            if len(check) != 9:
                return False
    else:
        return True

for case in range(T):
    data = [list(map(int,input().split())) for _ in range(9)]
    zip_data = list(zip(*data))

    if check_sdoku(data) and check_sdoku(zip_data) and grid_check(data):
        print('#{} {}'.format(case + 1, 1))
    else:
        print('#{} {}'.format(case + 1, 0))




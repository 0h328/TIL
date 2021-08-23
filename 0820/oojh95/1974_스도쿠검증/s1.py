import sys
sys.stdin = open('input.txt')
def check_rc(arr):
    for i in range(9):
        cnt = [0] * 10
        cnt2 = [0] * 10
        for j in range(9):
            cnt[arr[i][j]] += 1
            cnt2[arr[j][i]] += 1
            if cnt[arr[i][j]] == 2 or cnt2[arr[j][i]] == 2:
                return 0
    return 1
def check_box(arr):
    for i in range(0, 9, 3):

        for j in range(0, 9, 3):
            cnt = [0] * 10
            for k in range(3):
                for l in range(3):
                    cnt[arr[i+k][j+l]] += 1
                    if cnt[arr[i+k][j+l]] == 2:
                        return 0
    return 1

T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    if check_rc(arr) and check_box(arr):
        print('#{} 1'.format(test_case))
    else:
        print('#{} 0'.format(test_case))


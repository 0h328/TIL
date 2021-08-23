import sys
sys.stdin = open('input.txt')


def rotation(angle, arr):
    if angle == 0:  # angle이 0일때까지 회전
        return arr

    temp = deepcopy(arr)  # 90도 회전해야 하므로 기존 2차원 리스트에서 깊은 복사
    for x in range(N):
        for y in range(N):
            temp[x][y] = arr[N-1-y][x]  # 90도 회전

    return rotation((angle-90)%361, temp)  # 재귀 반복


from copy import deepcopy

T = int(input())
for test in range(10):
    N = int(input())
    N_list = [list(map(int, input().split())) for _ in range(N)]

    result_90 = rotation(90, N_list)
    result_180 = rotation(180, N_list)
    result_270 = rotation(270, N_list)

    print('#{}'.format(test + 1))
    for j in range(N):  # 행을 반복
        print(*result_90[j], sep='', end=' ')
        print(*result_180[j], sep='', end=' ')
        print(*result_270[j], sep='')

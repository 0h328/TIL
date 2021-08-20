import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    # 90도
    arr_90 = [[''] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            arr_90[i][j] = arr[N - 1 - j][i]
    # 180도
    arr_180 = [[''] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            arr_180[i][j] = arr[N - 1 - i][N - 1 - j]
    # 270도
    arr_270 = [[''] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            arr_270[i][j] = arr[j][N - 1 - i]

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr_90[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr_180[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr_270[i][j], end='')
        print()

##############################################################
def rotation(nums):
    tmp = [[''] * N for i in range(N)]

    for i in range(N):
        for j in range(N):
            # 회전하는 함수
            tmp[j][N - 1 - i] = nums[i][j]
    return tmp


def result(nums, col):
    for i in range(N):
        for j in range(N):
            ans[i][col] += nums[i][j]


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [input().split() for _ in range(N)]
#
#     ans = [[''] * 3 for _ in range(N)]
#     # 90도를 3번 돌린다.
#     for i in range(3):
#         arr = rotation(arr)
#         result(arr, i)
#
#     print("#{}".format(tc))
#     for i in range(N):
#         for j in range(3):
#             print(ans[i][j], end=" ")
#         print()

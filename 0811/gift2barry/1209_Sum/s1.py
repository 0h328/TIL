import sys
sys.stdin = open('input.txt')

# thought process:
# 가로줄 합
# 세로줄 합
# 대각선줄 합
# 리스트에 넣어서 가장 큰 값 리턴

T = 10                  # 총 루프 횟수 10 회
for _ in range(T):

    N = int(input())                        # problem number
    arr = [list(map(int, input().split())) for _ in range(100)]     # input 2차원 배열

    maxV = []                               # 행,열,대각선 순회 총 합들을 담을 리스트

    #가로 총 합들
    for i in range(len(arr)):
        total_1 = 0
        for j in range(len(arr[i])):
            total_1 += arr[i][j]
        maxV.append(total_1)

    #세로 총 합들
    for i in range(len(arr)):
        total_2 = 0
        for j in range(len(arr[i])):
            total_2 += arr[j][i]
        maxV.append(total_2)

    #negative대각선 총 합
    for i in range(len(arr)):
        total_3 = 0
        for j in range(len(arr)):
            if i == j:
                total_3 += arr[i][j]
        maxV.append(total_3)

    #positive대각선 총 합
    for i in range(len(arr)):
        total_4 = 0
        for j in range(len(arr)):
            if i + j == len(arr):           # +대각선에 위치한 i와 j의 합은 항상 = N
                total_4 += arr[i][j]
        maxV.append(total_4)

    ans = max(maxV)
    print('#{} {}'.format(N, ans))



# #binary search

# def binarySearch(a, key):
#     start = 0
#     end = len(a)-1
#     while start <= end:
#         middle = (start + end) // 2     # 몴을 구하니까 정수를 반환, 가운데 2개중
#         if a[middle] == key:
#             return True
#         elif a[middle] > key:
#             end = middle - 1
#         else:
#             start = middle + 1
#     return False
#
# print(binarySearch([1, 2, 3, 4], 4))

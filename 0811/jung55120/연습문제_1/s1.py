import sys
sys.stdin = open('input.txt')

tc = int(input())
point1, point2 = tc, tc
arr = [list(map(int, input().split())) for _ in range(tc)]
print(arr)
# [
# [9, 20, 2, 18, 11],
# [19, 1, 25, 3, 21],
# [8, 24, 10, 17, 7],
# [15, 4, 16, 5, 6],
# [12, 13, 22, 23, 14]
# ]

# 행 우선 순회
arr_1 = [[0] * tc for _ in range(tc)]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr_1[i][j] = arr[i][j]

print(arr_1)

# 열 우선 순회
arr_2 = [[0] * tc for _ in range(tc)]
for j in range(len(arr[0])):
    for i in range(len(arr)):
        arr_2[i][j] = arr[j][i]

print(arr_2)

# 지그재그 정렬
arr_3 = [[0] * tc for _ in range(tc)]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr_3[i][j] = arr[i][j+(point2-1-2*j)*(i%2)]

print(arr_3)

# 전치 행렬
arr_4 = [[0] * tc for _ in range(tc)]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr_4[i][j] = arr[i][j]
for i in range(tc):
    for j in range(tc):
        if i < j :
            arr_4[i][j], arr_4[j][i] = arr[j][i], arr[i][j]

print(arr_4)
import sys

sys.stdin = open('input.txt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 1. 행 우선 출력
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end=' ')

print()
# 2. 열 우선 출력
for j in range(len(arr)):
    for i in range(len(arr[0])):
        print(arr[i][j], end=' ')

print()
# 3. 지그재그 출력
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j + (len(arr[0]) - 1 - 2*j) * (i % 2)], end=' ')

print()
# 4. 전치행렬
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)
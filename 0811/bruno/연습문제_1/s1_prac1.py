import sys
sys.stdin = open('input.txt')

n = m = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 행 우선 순회
print(arr)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')
print()
# 열 우선 순회
for j in range(len(arr[0])):
    for i in range(len(arr)):
        print(arr[i][j], end=' ')
print()
# 지그재그
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j + (m-1-2*j) * (i % 2)], end=' ')
print()
# 전치행렬
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i > j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)
import sys
sys.stdin = open("input.txt")

T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]

# 행 우선 순회
for i in range(T):
    for j in range(T):
        print(arr[i][j], end=' ')

print()

# 열 우선 순회
for i in range(T):
    for j in range(T):
        print(arr[j][i], end=' ')

print()

# 지그재그
for i in range(T):
    if i % 2:
        for j in range(T-1, -1, -1):
            print(arr[i][j], end=' ')
    else:
        for j in range(T):
            print(arr[i][j], end=' ')

print()

# 전치행렬
for i in range(T):
    for j in range(T):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)
import sys
sys.stdin = open('input.txt')

n = int(input())

arr = [] # 2차원 배열 안에 숫자 채우기
for _ in range(n):
    in_arr = list(map(int, input().split()))
    arr.append(in_arr)

# 1. 행우선
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
print()

# 2. 열우선
for j in range(n):
    for i in range(n):
        print(arr[i][j], end=' ')
print()

# 3. 지그재그
for i in range(n):
    for j in range(n):
        print(arr[i][j + (n-1-2*j) * (i%2)], end=' ')
print()

# 4. 전치행렬
for i in range(n):
    for j in range(n):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)
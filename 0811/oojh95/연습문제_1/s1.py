import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range (N)]
print(arr)

# step1. 행우선
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
print()
# step2. 열우선
for i in range(N):
    for j in range(N):
        print(arr[j][i], end=' ')
print()
# step3. 지그재그
for i in range(N):
    for j in range(N):
        print(arr[i][j + (N - 1 - 2 * j) * (i % 2)], end=' ')
print()
# step4. 전치행렬
for i in range(N):
    for j in range(N):
        if j > i:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)
import sys

sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print('행우선')
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')

print('\n열우선')
for j in range(N):
    for i in range(N):
        print(arr[i][j], end=' ')

print('\n지그재그')
for i in range(N):
    for j in range(N):
        print(arr[i][j - (2*j + 1) * (i % 2)], end=' ')

print('\n전치행렬')
for i in range(N):
    for j in range(N):
        if i > j:   # 이 조건이 없으면 바뀌지 않음. i < j와 동일
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)
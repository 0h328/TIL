import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = [[] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

print(arr)

# print([list(map(int, input().split())) for _ in range(N)])

print('\n', '1. 행 우선 선회', sep='')
#1. 행 우선 선회
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()

print('\n', '2. 열 우선 선회', sep='')
#2. 열 우선 선회
for i in range(M):
    for j in range(N):
        print(arr[j][i], end=' ')
    print()
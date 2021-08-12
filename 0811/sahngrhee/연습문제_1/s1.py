import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        print(arr[i][j], end = ' ')
print()

for j in range(N):
    for i in range(N):
        print(arr[i][j], end = ' ')
print()

for i in range(N):
    for j in range(N):
        print(arr[i][j + (N-1-2*j) * (i %2)], end = ' ')
print()

for i in range(N):
    for j in range(N):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print(arr)





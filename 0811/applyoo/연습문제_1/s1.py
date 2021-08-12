import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int ,input().split())) for _ in range(N)]

print()
for row in arr:
    print(*row, end=' ')

print()
for col in zip(*arr):
    print(*col, end=' ')

print()
confirm = True
for row in arr:
    if confirm:
        print(*row, end=' ')
    else:
        print(*row[::-1], end=' ')
    confirm = not confirm

print()
for i in range(len(arr)):
    for j in range(len(arr)):
        if i > j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)
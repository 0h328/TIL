import sys
sys.stdin = open('input.txt')

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

# 1. 행우선
for row in arr:
    for e in row:
        print(e, end=' ')
print()

# 2. 열우선
for col in zip(*arr):
    for e in col:
        print(e, end=' ')
print()
# 3. 지그재그
for i in range(N):
    if i%2 == 0:
        print(' '.join(map(str, arr[i])), end=' ')
    else:
        print(' '.join(map(str, reversed(arr[i]))), end=' ')
print()
# 4. 전치행렬
print(list(zip(*arr)))

# 9 20 2 18 11 19 1 25 3 21 8 24 10 17 7 15 4 16 5 6 12 13 22 23 14
# 9 19 8 15 12 20 1 24 4 13 2 25 10 16 22 18 3 17 5 23 11 21 7 6 14
# 9 20 2 18 11 21 3 25 1 19 8 24 10 17 7 6 5 16 4 15 12 13 22 23 14
# [[9, 19, 8, 15, 12], [20, 1, 24, 4, 13], [2, 25, 10, 16, 22], [18, 3, 17, 5, 23], [11, 21, 7, 6, 14]]
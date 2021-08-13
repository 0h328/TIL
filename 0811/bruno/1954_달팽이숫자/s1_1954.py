import sys
sys.stdin = open('input.txt')

n = int(input())
arr = [[0] * n for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
cnt = 1
i = 0
j = -1
k = 0

while cnt <= n*n:
    ni, nj = i+di[k], j+dj[k]

    if ni <= n-1 and nj <= n-1 and arr[ni][nj] == 0:
        arr[ni][nj] = cnt
        cnt += 1
        i, j = ni, nj
    else:
        k = (k+1) % 4

for i in range(len(arr)):
    for x in arr[i]:
        print(x, end=' ')
    print()

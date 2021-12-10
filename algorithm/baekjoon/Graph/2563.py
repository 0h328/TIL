import sys
sys.stdin = open('input.txt')
'''
3
3 7
15 7
5 2
'''

N = int(input())

arr = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] += 1

    area = 0
    for k in range(100):
        for l in range(100):
            if arr[k][l] > 0:
                area += 1

print(area)



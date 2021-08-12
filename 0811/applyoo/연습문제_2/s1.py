import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int ,input().split())) for _ in range(N)]

xy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for i, j in xy:
    print(arr[1+i][1+j])
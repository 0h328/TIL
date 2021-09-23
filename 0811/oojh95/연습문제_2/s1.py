import sys
sys.stdin = open('input.txt')
from pandas import DataFrame
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(4):
    print(arr[1 + dy[i]][1 + dx[i]])

print(DataFrame(arr))
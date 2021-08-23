import sys

sys.stdin = open('input.txt')
from pandas import DataFrame
T = int(input())
data = []
for test in range(T):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x = 1
y = 1

for h in range(4):
    nx = x + dx[h]
    ny = y + dy[h]

print(DataFrame(data))

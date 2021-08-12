import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

# for test_case in range(1, 11):
T = int(input())
arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
#print(DataFrame(arr))
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

r = 99
for i in range(100):
    if arr[99][i] == 2:
        c = i

while r != 0:
    if arr[r+dr[2]][c+dc[2]] == 0 and arr[r+dr[0]][c+dc[0]] == 0:
        r = r + dr[3]
        c = c + dc[3]
    else:
        if arr[r+dr[2]][c+dc[2]] == 1:
            r = r + dr[2]
            c = c + dc[2]
        elif arr[r+dr[0]][c+dc[0]] == 1:
            r = r + dr[0]
            c = c + dc[0]

# 모르겠습니다.







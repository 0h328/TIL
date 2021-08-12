import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

# for test_case in range(1, 11):
T = int(input())
arr = [[0]+list(map(int, input().split()))+[0] for _ in range(10)]
#print(DataFrame(arr))
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
di = 0
r = 9
for i in range(12):
    if arr[9][i] == 2:
        c = i

while r != 0:
    if arr[r+dr[2]][c+dc[2]] == 0 and arr[r+dr[0]][c+dc[0]] == 0:
        di = 3
        r = r + dr[di]
        c = c + dc[di]

    elif arr[r + dr[3]][c + dc[3]] == 0 and arr[r + dr[1]][c + dc[1]] == 0:
        r = r + dr[di]
        c = c + dc[di]

    elif arr[r+dr[2]][c+dc[2]] == 1:
        di = 2
        r = r + dr[di]
        c = c + dc[di]

    elif arr[r+dr[0]][c+dc[0]] == 1:
        di = 0
        r = r + dr[di]
        c = c + dc[di]

 # 아직도 모르겠다.


















import sys
sys.stdin = open('input.txt')

T = int(input())

arr = [list(map(int,input().split())) for _ in range(T)]

di = [-1,1,0,0]
dj = [0,0,-1,1]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 5:
            for k in range(4):
                print(arr[i+di[k]][j+dj[k]])
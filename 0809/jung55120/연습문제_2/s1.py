import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
print(N,M)

arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)


#1. 행 우선 순회
for i in range(len(arr)) :
    for j in range(len(arr[i])) :
        print(arr[i][j])

#2. 열 우선 순회
for j in range(len(arr[0])) :
    for i in range(len(arr)) :
        print(arr[i][j])
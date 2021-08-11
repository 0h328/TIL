import sys
sys.stdin = open('input.txt')
# 인풋값 불러오기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 배열 순회:

# 1. 행 우선 순회
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')

print() # 칸 띄우는 용도

# 2. 열 우선 순회
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[j][i], end=' ')

print() # 칸 띄우는 용도

# 열 우선 순회 ver.2
for j in range(len(arr[0])):
    for i in range(len(arr)):
        print(arr[i][j], end=' ')

print() # 칸 띄우는 용도

# 지그재그 순회
#
# thought process:
# 홀수 우측으로 순회, 짝수 좌축으로 순회
for i in range(len(arr)):
        if i % 2 == 0:       #짝수 일 경우
            for j in range(len(arr[i])):
                print(arr[i][j], end=' ')
        else:                #홀수 일 경우
            for j in range(len(arr[i])-1, -1, -1):
                print(arr[i][j], end=' ')

print() # 칸 띄우는 용도

# 전치행렬
# thought process:
# 먼저 종이에 적고 생각좀..
for i in range(N):
    for j in range(N):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
            print(arr[i][j], arr[j][i], end=' ')

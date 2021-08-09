import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 행 / 열의 길이 받기
N, M = map(int, input().split())
num = []
for i in range(N):
    my_num = list(map(int, input().split()))
    num.append(my_num)
print(num)

#1. 행 우선 순회
for row in range(N):
    for col in range(M):
        print(num[row][col], end='\t')
    print()

#2. 열 우선 순회
for col in range(M):
    for row in range(N):
        print(num[row][col], end='\t')
    print()
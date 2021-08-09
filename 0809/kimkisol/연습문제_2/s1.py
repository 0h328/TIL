import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 행 / 열의 길이 받기
row, col = map(int, input().split())

#1. 행 우선 순회
# num = []
# for i in range(row):
#     row_list = list(map(int, input().split()))
#     num.append(row_list)
# print(num)

#2. 열 우선 순회
num = []
for i in range(col):
    row_list = list(map(int, input().split()))
    for j in range(row):
        num.append(row_list)
print(num)
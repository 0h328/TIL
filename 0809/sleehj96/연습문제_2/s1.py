import sys
sys.stdin = open('input.txt')

r, c = map(int, input().split())

# print(r, c)

# arr = []
# for _ in range(r):
#     arr.append(list(map(int, input().split())))

arr = [list(map(int, input().split())) for _ in range(r)]
print(arr)

# # #1. 행 우선 순회
print('행 우선 순회')
for row in range(r):
    for col in range(c):
        print(arr[row][col])

print()

#2. 열 우선 순회
print('열 우선 순회')
for col in range(c):
    for row in range(r):
        print(arr[row][col])
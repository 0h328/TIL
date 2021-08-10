import sys
sys.stdin = open('input.txt')

data = list(map(int, input().split()))                  # 주어진 데이터의 목록
for j in range(len(data) - 1, 0, -1):                   #
    for i in range(0, j):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
print(*data)

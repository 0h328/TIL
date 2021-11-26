import sys

sys.stdin = open('input.txt')


def rotate(key):
    return list(zip(*key))


N, M = map(int, input().split())  # 3,4

numbers = [list(map(int, input().split())) for _ in range(N)]
print(numbers)

# 행 우선순회 출력
for i in range(N):
    for j in range(M):
        print(numbers[i][j], end=' ')
print()

# 열 우선순회
for i in range(M):
    for j in range(N):
        print(numbers[j][i], end=' ')
print()

numbers2 = rotate(numbers)

for i in range(M):
    for j in range(N):
        print(list(zip(*numbers))[i][j], end=' ')
print()

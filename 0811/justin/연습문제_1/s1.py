import sys
sys.stdin = open('input.txt')

#1.
N = int(input())

#1-1.
# matrix = []
# for _ in range(N):
#     matrix.append(list(map(int, input().split())))

#1-2.
matrix = [list(map(int, input().split())) for _ in range(N)]
print('------------------------------')


#2. 행 우선
for i in range(N):
    for j in range(N):
        print(matrix[i][j], end=' ')
print()

#3. 열 우선
for i in range(N):
    for j in range(N):
        print(matrix[j][i], end=' ')
print()

#4. 지그재그
for i in range(N):
    for j in range(N):
        # (i % 2)는 홀/짝 -> 0/2/4/6 ...
        print(matrix[i][j + (N-1-2*j) * (i%2)], end=' ')
print()

#5. 전치 행렬(행과 열을 반대로)
for i in range(N):
    for j in range(N):
        if i < j:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print(matrix)
# 혹은 zip & unpacking 활용
data = [list(data) for data in zip(*matrix)]
print(data)

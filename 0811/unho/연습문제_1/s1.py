import sys
sys.stdin = open('input.txt')

num = int(input())
num_list = [list(map(int, input().split())) for _ in range(num)]

for i in range(num):                        # 행우선
    for j in range(num):
        print(num_list[i][j], end=' ')

print()

for i in range(num):                        # 열우선
    for j in range(num):
        print(num_list[j][i], end=' ')

print()

for i in range(num):                        # 지그재그
    for j in range(num):
        print(num_list[i][j + (num - 1 - 2*j)*(i%2)], end=' ')

print()
new_list = []

for i in range(num):                        # 전치행렬
    tmp_list = []
    for j in range(num):
        tmp_list.append(num_list[j][i])
    new_list.append(tmp_list)
print(new_list)
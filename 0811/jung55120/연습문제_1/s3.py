import sys
sys.stdin = open('input.txt')

N = int(input())

my_list = [list(map(int, input().split())) for n in range(N)]

# 행 우선 순회
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[i][j], end=' ')
print()

# 열 우선 순회
for i in range(len(my_list[0])):
    for j in range(len(my_list)):
        print(my_list[j][i], end=' ')
print()

# 지그재그 순회
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        if i % 2 == 0:
            print(my_list[i][j], end=' ')
        else:
            print(my_list[i][-1-j], end=' ')
print()

# 전치행렬
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        if i < j:
            my_list[i][j], my_list[j][i] = my_list[j][i], my_list[i][j]
print(my_list)


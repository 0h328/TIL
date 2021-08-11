import sys
sys.stdin = open('input.txt')

T = int(input())

data_list = [list(map(int,input().split())) for _ in range(T)]

# 행 우선
for i in range(len(data_list)):
    for j in range(len(data_list[i])):
        print(data_list[i][j], end=' ')
print()
# 열 우선
for j in range(len(data_list[0])):
    for i in range(len(data_list)):
        print(data_list[i][j], end=' ')
print()
# 지그재그
for i in range(len(data_list)):
    if i%2:
        for j in range(len(data_list[i])-1,-1,-1):
            print(data_list[i][j], end=' ')
    else:
        for j in range(len(data_list[i])):
            print(data_list[i][j], end=' ')
print()
# 전치행렬
for i in range(len(data_list)):
    for j in range(len(data_list[i])):
        if i < j:
            data_list[i][j], data_list[j][i] = data_list[j][i], data_list[i][j]
print(data_list)



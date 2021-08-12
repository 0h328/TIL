import sys
sys.stdin = open("input.txt")

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

lst = []

for i in range(len(A)):
    lst.append(len(A[i]))

max_value = lst[0]
for i in lst:
    if max_value < i:
        max_value = i

A_list = []

for i in range(len(A)):
    for j in range(max_value):
        try:
            if i % 2 == 0:
                A_list.append(A[i][j])
            else:
                while N-1-j >= 0:
                    A_list.append(A[i][N-1-j])
                    break
        except IndexError:
            pass

print(A_list)

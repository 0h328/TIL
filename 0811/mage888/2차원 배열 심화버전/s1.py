import sys
sys.stdin = open("input.txt")

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

length_A = []

for l in range(len(A)):
    length_A.append(len(A[l]))

max_value = length_A[0]
for k in length_A:
    if max_value < k:
        max_value = k

i = 0
for i in range(max_value): #5 : 0~4
    for j in range(len(A)): # i = 0 : 0~4 / i = 1 : 0~2 / i = 2 : 0~3 / i = 3 : 0~4 / i = 4 : 0~1

        try:
            print(A[j][i], end=' ')
        except IndexError:
            pass
    i += 1
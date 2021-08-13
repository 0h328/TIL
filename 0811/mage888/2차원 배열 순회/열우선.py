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
for i in range(max_value):
    for j in range(len(A)):

        try:
            print(A[j][i], end=' ')
        except IndexError:
            pass
    i += 1


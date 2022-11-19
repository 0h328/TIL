import sys
sys.stdin = open('input.txt')

A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

tmp = 0
if P > C:
    tmp = B+(P-C)*D
else:
    tmp = B

if A*P > tmp:
    print(tmp)
else:
    print(A*P)

import sys
sys.stdin = open('input.txt')

A, B, C = map(int, input().split(" "))
D = int(input())

s1 = (C+D)%60
m1 = (C+D)//60
m2 = (B+m1)%60
h1 = (B+m1)//60
h2 = (A+h1)%24

print(h2, m2, s1)
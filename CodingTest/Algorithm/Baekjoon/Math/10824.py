import sys
sys.stdin = open('input.txt')

A, B, C, D = input().split()

print(int(A+B)+int(C+D))
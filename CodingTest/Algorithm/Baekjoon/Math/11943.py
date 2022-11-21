import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())
C, D = map(int, input().split())

print(min(A+D, B+C))
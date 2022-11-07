import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())
print((A+B)*(A-B))
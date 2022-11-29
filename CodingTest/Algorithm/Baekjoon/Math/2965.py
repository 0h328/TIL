import sys
sys.stdin = open('input.txt')

A, B, C = map(int, input().split())
print(max(B-A-1, C-B-1))
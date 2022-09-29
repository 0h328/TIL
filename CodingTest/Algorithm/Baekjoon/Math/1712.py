import sys
sys.stdin = open('input.txt')

A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    print(int(A/(C-B)+1))
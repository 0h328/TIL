import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())
timer = int(input())

A += timer // 60
B += timer % 60

if B >= 60:
    A += 1
    B -= 60
if A >= 24:
    A -= 24

print(A, B)
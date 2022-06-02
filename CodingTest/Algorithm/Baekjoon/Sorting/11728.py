import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

ans = A+B
ans.sort()

print(*ans)
import sys
sys.stdin = open('input.txt')

# (수업)
T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
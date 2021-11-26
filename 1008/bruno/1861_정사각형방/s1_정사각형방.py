import sys
sys.stdin = open('input.txt')

T = int(input())
for x in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

import sys
sys.stdin = open('input.txt')

T = int(input())

N = int(input())

check = [[0]*N for _ in range(N)]

for i in range(N):

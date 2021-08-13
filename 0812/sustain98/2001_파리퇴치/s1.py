import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1,t+1):
    n, m = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n-m):
        

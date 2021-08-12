import sys
sys.stdin = open('input.txt')

for i in range(10):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

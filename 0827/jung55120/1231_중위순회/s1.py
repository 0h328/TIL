import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    node = [0] * (N + 1)
    for i in range(N):
        
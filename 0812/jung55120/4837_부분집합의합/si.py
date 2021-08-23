import sys
sys.stdin = open('input.txt')

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())
for t in range(1, T+1):
    num, result = map(int, input().split())

    for i in range(1 << n):
        for j in range(n):
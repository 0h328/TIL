import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
print(abs(N-M))
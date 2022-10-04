import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
print(N-1+(M-1)*N)
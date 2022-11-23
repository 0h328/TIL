import sys
sys.stdin = open('input.txt')

N, M, K = map(int, input().split())
n = K // M
m = K % M
print(n, m)
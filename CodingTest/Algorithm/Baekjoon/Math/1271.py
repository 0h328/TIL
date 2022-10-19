import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
print(n//m)
print(n%m)
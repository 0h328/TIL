import sys

sys.stdin = open("input.txt")

n, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

print(n, k, lst)
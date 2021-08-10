import sys

sys.stdin = open('input.txt')

h, w = map(int, input().split())
in_list = [list(map(int, input().split())) for _ in range(h)]

print(in_list)
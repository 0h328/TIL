import sys
sys.stdin = open('input.txt')


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    code = [list(map(int, input())) for _ in range(N)]


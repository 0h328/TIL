import sys
sys.stdin = open('input.txt')

M, F = map(int, input().split())
while not (M == 0 and F == 0):
    print(M+F)
    M, F = map(int, input().split())
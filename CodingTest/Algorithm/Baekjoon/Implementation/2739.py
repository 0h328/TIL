import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(1, 10):
    print(str(N), end=' ')
    print('*', end=' ')
    print(i, end=' ')
    print('=', end=' ')
    print(N * i)
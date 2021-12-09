import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(N):
    print(i * ' ' + (N-i) * '*')

import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1, t+1):
    n, m = map(int, input().split())
    l = input().split()
    print('#{} {}'.format(idx, l[m % n]))
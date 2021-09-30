import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1, t+1):
    n, m = map(int, input().split())
    if bin(m)[-n:] == '1'*n:
        res = 'ON'
    else:
        res = 'OFF'
    print('#{} {}'.format(idx, res))
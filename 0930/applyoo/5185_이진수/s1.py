import sys
sys.stdin = open('input.txt')

t = {}
for i in range(0, 16):
    if i < 10: t[str(i)] = '{0:0>4}'.format(str(bin(i))[2:])
    else: t[chr(55+i)] = '{0:0>4}'.format(str(bin(i))[2:])

T = int(input())
for tc in range(1, T+1):
    N, W = input().split()
    print('#{0} {1}'.format(tc, ''.join([t[i] for i in W])))

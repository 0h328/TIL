import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1, t+1):
    n, number = input().split()
    res = ''
    for i in number:
        res += ('0000' + bin(int(i, 16))[2:])[-4:]
    print('#{} {}'.format(idx, res))
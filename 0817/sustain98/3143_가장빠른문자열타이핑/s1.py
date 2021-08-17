import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1, t+1):
    A, B = input().split()
    cnt = len(A.replace(B, '_'))

    print('#{} {}'.format(idx, cnt))


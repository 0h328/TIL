import sys
sys.stdin = open('input.txt')

N = int(input())

if N == 1:
    print('*')
elif N >= 2:
    for i in range(1, N+1):
        if i == 1:
            print((N-i) * ' ' + '*')
        elif i == 2:
            print((N-i) * ' ' + '* ' + '*')
        else:
            print((N-i) * ' ' + (i-1) * '* ' + (N-i) * '' + '*')




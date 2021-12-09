import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(1, N+1):
    if i == 1:
        print((N-i) * ' ' + '*')
    elif i == 2:
        print((N-i) * ' ' + '*' + (i-1) * ' ' + '*')
    else:
        print((N-i) * ' ' + '*' + (2*i-3) * ' ' + '*')


import sys
sys.stdin = open('input.txt')

N = list(input())
N.sort(reverse=True)
s = 0

if '0' not in N:
    print(-1)
else:
    for i in N:
        s += int(i)
    if s % 3 != 0:
        print(-1)
    else:
        print(''.join(N))

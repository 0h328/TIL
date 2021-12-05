import sys
sys.stdin = open('input.txt')

a, b = input().split()

c = a[::-1]
d = b[::-1]

if c > d:
    print(c)
else:
    print(d)

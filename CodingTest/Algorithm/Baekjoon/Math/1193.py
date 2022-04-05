import sys
sys.stdin = open('input.txt')

X = int(input())

tmp = 1
while X > tmp:
    X -= tmp
    tmp += 1

if tmp % 2 == 0:
    a = X
    b = tmp - X + 1
else:
    a = tmp - X + 1
    b = X

print(a, '/', b, sep='')
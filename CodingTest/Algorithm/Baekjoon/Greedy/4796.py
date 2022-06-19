import sys
sys.stdin = open('input.txt')

tmp = 0
while True:
    tmp += 1
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0:
        break

    x = V//P
    y = V%P

    if L < y:
        y = L
    print("Case %d: %d" %(tmp, x*L+y))
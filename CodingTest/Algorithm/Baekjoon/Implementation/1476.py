import sys
sys.stdin = open('input.txt')

E, S, M = map(int, input().split())

cnt = 1
a = b = c = 1

while True:
    if E == a and S == b and M == c:
        print(cnt)
        break
    a += 1
    b += 1
    c += 1
    cnt += 1
    if a >= 16:
        a -= 15
    if b >= 29:
        b -= 28
    if c >= 20:
        c -= 19


import sys
sys.stdin = open('input.txt')

N, Kim, Lim = map(int, input().split())
cnt = 0
while Kim != Lim:
    Kim -= Kim // 2
    Lim -= Lim // 2
    cnt += 1

print(cnt)
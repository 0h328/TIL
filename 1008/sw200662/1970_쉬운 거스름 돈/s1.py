import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print('#{}'.format(tc))
    cnt = 0
    while N >= 50000:
        N -= 50000
        cnt += 1
    print(cnt, end=' ')
    cnt = 0
    while N >= 10000:
        N -= 10000
        cnt +=1
    print(cnt, end=' ')
    cnt = 0
    while N >= 5000:
        N -= 5000
        cnt += 1
    print(cnt, end=' ')
    cnt = 0
    while N >= 1000:
        N -= 1000
        cnt += 1
    print(cnt, end=' ')
    cnt = 0
    while N >= 500:
        N -= 500
        cnt += 1
    print(cnt, end=' ')
    cnt = 0
    while N >= 100:
        N -= 100
        cnt += 1
    print(cnt, end=' ')
    cnt = 0
    while N >= 50:
        N -= 50
        cnt += 1
    print(cnt, end=' ')
    cnt = 0
    while N >= 10:
        N -= 10
        cnt += 1
    print(cnt)
    cnt = 0

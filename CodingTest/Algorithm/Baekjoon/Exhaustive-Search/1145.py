import sys
sys.stdin = open('input.txt')

a = list(map(int, input().split()))
N = min(a)
while True:
    cnt = 0
    for i in range(5):
        if N % a[i] == 0:
            cnt += 1
    if cnt > 2:
        print(N)
        break
    N += 1
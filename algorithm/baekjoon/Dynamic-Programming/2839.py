import sys
sys.stdin = open('input.txt')

N = int(input())
cnt = 0

while N >= 0:
    if N % 5 == 0:
        cnt += N // 5
        print(cnt)
        exit()

    N -= 3
    cnt += 1

print(-1)

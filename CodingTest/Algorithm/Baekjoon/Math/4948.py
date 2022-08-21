import sys
sys.stdin = open('input.txt')

num = []

for i in range(2, 246913):
    cnt = 0

    for p in range(2, int(i**0.5)+1):
        if i % p == 0:
            cnt += 1
            break

    if cnt == 0:
        num.append(i)

while True:
    n = int(input())
    res = 0

    if n == 0:
        break

    for i in num:
        if n < i <= 2*n:
            res += 1

    print(res)
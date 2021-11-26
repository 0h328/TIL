import sys
sys.stdin = open('input.txt', encoding='UTF-8')

for _ in range(10):
    tc = int(input())
    p = input()
    t = input()

    n, m = len(t), len(p)

    cnt = 0
    for i in range(n-m+1):
        if t[i:i+m] == p:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
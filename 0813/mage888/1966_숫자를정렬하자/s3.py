import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = list(map(int,input().split()))

    cnt = [0] * (max(a) + 1)
    temp = [0] * n

    for i in range(n):
        cnt[a[i]] += 1

    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]

    for i in range(n):
        cnt[a[i]] -= 1
        temp[cnt[a[i]]] = a[i]

    print('#{}'.format(tc), end=' ')
    print(*temp)
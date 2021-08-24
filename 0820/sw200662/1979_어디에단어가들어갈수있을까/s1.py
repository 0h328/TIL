import sys

sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    list1 = []
    for z in range(N):
        k = list(map(int, input().split()))
        list1.append(k)
    list2 = list(zip(*list1))
    ans = 0
    for c in list1:
        cnt = 0
        for b in range(N):
            if c[b] == 1:
                cnt += 1
                if b == (N - 1) and cnt == K:
                    ans += 1
            elif c[b] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
            elif b == (N - 1) and cnt == K:
                ans += 1
    for d in list2:
        cnt = 0
        for e in range(N):
            if d[e] == 1:
                cnt += 1
                if e == (N-1) and cnt == K:
                    ans += 1
            elif d[e] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
            elif d == (N - 1) and cnt == K:
                ans += 1

    print('#{} {}'.format(i+1,ans))
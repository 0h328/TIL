import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1,t+1):
    k, n, m = map(int, input().split())
    charge = list(sorted(map(int, input().split()))) + [n]
    loc = k
    cnt = 0

    for i in range(m):
        if charge[i] <= loc < charge[i+1]:
            cnt += 1
            loc = charge[i] + k
        else:
            continue

        if loc >= n:
            break

    if loc < n:
        cnt = 0
    print('#{} {}'.format(idx, cnt))



#3
#0
#4

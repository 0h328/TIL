import sys
sys.stdin = open('input.txt')


def pre_order(n):
    global cnt
    if n:
        cnt += 1
        pre_order(left[n])
        pre_order(right[n])


T = int(input())
for test in range(T):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    cnt = 0

    for i in range(E):
        p, c = edge[i * 2], edge[i * 2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    pre_order(N)
    print('#{} {}'.format(test+1, cnt))

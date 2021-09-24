import sys
sys.stdin = open('input.txt')


def in_order(n):
    global cnt
    if n:
        in_order(left[n])
        cnt += 1
        if n == 1:
            result[0] = cnt
        if n == N//2:
            result[1] = cnt
        in_order(right[n])


T = int(input())
for test in range(T):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    result = [0, 0]
    cnt = 0

    for i in range(2, N+1):
        if i % 2:
            right[i//2] = i
        else:
            left[i//2] = i

    in_order(1)
    print('#{}'.format(test+1), end=' ')
    print(*result)

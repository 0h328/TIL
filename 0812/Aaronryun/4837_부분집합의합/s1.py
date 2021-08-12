import sys

sys.stdin = open('input.txt')

T = int(input())

for test in range(T):
    N, K = map(int, input().split())

    A = list(range(1, 13))

    n = len(A)

    cnt = 0
    for i in range(1 << n):
        check = []
        for j in range(n):
            if i & (1 << j):
                check.append(A[j])
        if len(check) == N and sum(check) == K:
            cnt += 1

    print('#{} {}'.format(test + 1, cnt))

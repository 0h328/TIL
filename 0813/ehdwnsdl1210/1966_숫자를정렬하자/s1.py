import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    L = list(map(str, input().split()))

    M = len(L)
    for i in range(M - 1):
        min_idx = i
        for j in range(i + 1, M):
            if int(L[min_idx]) > int(L[j]):
                min_idx = j
        L[i], L[min_idx] = L[min_idx], L[i]

    result = ' '.join(L)

    print('#{} {}'.format(tc, result))
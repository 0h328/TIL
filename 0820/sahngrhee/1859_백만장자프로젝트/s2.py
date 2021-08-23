def FMI(L):
    M = L[0]
    M_index = 0
    for i in range(len(L)):
        if L[i] > M:
            M = L[i]
            M_index = i
    return M, M_index

import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    P = list(map(int, input().split()))

    ans = 0
    while True:
        C, c = FMI(P)
        total = 0
        for i in range(c):
            total += C - P[i]
        ans += total

        if c == len(P)-1:
            break
        else:
            P = P[c + 1:len(P)]

    print('#{} {}'.format(test_case, ans))







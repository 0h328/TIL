import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    P = list(map(int, input().split()))

    total = 0
    while True:

        S = P[0:P.index(max(P))+1]
        a = []
        for s in S:
            a.append(max(S)-s)
        total += sum(a)
        if S == P:
            break
        P = P[P.index(max(P))+1:]

    print('#{} {}'.format(test_case, total))
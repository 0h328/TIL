import sys

sys.stdin = open("input.txt")

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    Q = []

    while C.count(0) != M-1:
        for m in range(M):
            if C[m] != 0:
                Q.append(C[m])

            if len(Q) == N:
                C[m+1-N] = Q.pop(0) // 2
            elif M - C.count(0) < N and C.count(0) != M-1:
                C[m+1-N] = Q.pop(0) // 2


    for i in range(len(C)):
        if C[i] == 1:
            print("#{} {}".format(t+1, i+1))

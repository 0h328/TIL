import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()

    N = len(A)
    M = len(B)

    i = 0
    j = 0
    cnt = 0

    while i < N and j < M:
        if B[j] != A[i+j]:
            break
        i += 1
        j += 1
    if j == M:
        cnt += 1

    print(cnt)

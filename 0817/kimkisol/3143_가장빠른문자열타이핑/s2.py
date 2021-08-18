import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    A, B = input().split()
    result = len(A)
    idx_A = 0
    idx_B = 0

    while idx_A < len(A):
        if A[idx_A] != B[idx_B]:
            idx_B = 0
        else:
            idx_B += 1
        if idx_B == len(B):
            result -= (len(B) - 1)
            idx_B = 0
        idx_A += 1

    print('#{} {}'.format(t, result))

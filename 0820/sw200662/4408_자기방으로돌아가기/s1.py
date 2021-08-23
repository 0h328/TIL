import sys

sys.stdin = open('input.txt')

T = int(input())
for i in range(T):
    N = int(input())
    list_1 = [0 for _ in range(401)]
    for _ in range(N):
        A, B = map(int, input().split())
        A = (A+1) // 2
        B = (B+1) // 2
        if A < B:
            for z in range(A, B+1):
                list_1[z] += 1
        else:
            for z in range(B, A+1):
                list_1[z] += 1
    print('#{} {}'.format(i + 1, max(list_1)))

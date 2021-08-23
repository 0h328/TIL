import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cnt = [0 for _ in range(5001)]
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            cnt[i] += 1
    P = int(input())
    C = [0 for _ in range(P)]
    for i in range(P):
        C[i] = int(input())
        C[i] = cnt[C[i]]
    print('#{}'.format(test_case), end=' ')
    print(*C, sep=' ')

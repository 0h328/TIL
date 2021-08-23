import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cnt = [0 for _ in range(401)]
    max_result = 1
    for i in range(N):
        A, B = map(int, input().split())
        if A > B:
            A, B = B, A
        if A % 2 == 0:
            A -= 1
        if B % 2 == 1:
            B += 1
        for j in range(A, B+1):
            cnt[j] += 1
            if cnt[j] > max_result:
                max_result = cnt[j]
    print('#{} {}'.format(test_case, max_result))

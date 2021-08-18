import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    cnt = 0
    i = 0
    while i < len(A) - len(B) + 1:
        if A[i:i+len(B)] == B:
            cnt += 1
            i += len(B)
        else:
            i += 1
    type_cnt = (len(A) - len(B) * cnt) + cnt
    print('#{} {}'.format(tc, type_cnt))
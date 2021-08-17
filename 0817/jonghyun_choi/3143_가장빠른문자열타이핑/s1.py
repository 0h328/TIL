import sys
sys.stdin = open('input.txt')

# Time Error 발생 코드
T = int(input())

for case in range(T):
    A, B = input().split()
    i = 0
    cnt = 0
    while i < len(A):
        if A[i] == B[0]:
            if A[i:i+len(B)] == B:
                cnt += 1
                i = i+len(B)
        else:
            i += 1
            cnt += 1

    print('#{} {}'.format(case + 1, cnt))

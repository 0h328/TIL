import sys
sys.stdin = open('input.txt')

T = int(input())

case_num = 1
while case_num <= T:
    A, B = input().split()
    len_a = len(A)
    len_b = len(B)

    cnt = 0

    # i = 0
    # while i < len_a - len_b + 1:
    #     if A[i] == B[0]:
    #         if A[i:i+len_b] == B:
    #             cnt += 1
    #             i += len_b
    #             continue
    #     i += 1

    # BruteForce 로 구현
    i = 0
    while i < len(A):
        j = 0
        while j < len(B):
            if A[i+j] != B[j]:
                i -= j
                break
            j += 1
        else:
            i += j - 1
            cnt += 1
        i += 1

    print('#{0} {1}'.format(case_num, len(A) - cnt * (len(B) - 1)))
    # break
    case_num += 1

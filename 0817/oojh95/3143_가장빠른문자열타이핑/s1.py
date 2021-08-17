import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    A, B = input().split()
    cnt = 0

    cnt = A.count(B)


    result = len(A) - cnt * len(B) + cnt
    print('#{} {}'.format(test_case, result, test_case))

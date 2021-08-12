import sys
sys.stdin = open('input.txt')


def binary_search(P, target):
    high = P
    low = 1
    cnt = 1

    while low <= high:
        mid = (high + low) // 2

        if mid == target:
            break
        elif mid > target:
            high = mid
            cnt += 1
        elif mid < target:
            low = mid
            cnt += 1

    return cnt


test_case = int(input())

for tc in range(1, test_case+1):
    P, A, B = map(int, input().split())
    cnt_a = 0
    cnt_b = 0

    cnt_a = binary_search(P, A)
    cnt_b = binary_search(P, B)

    if cnt_a > cnt_b:
        answer = 'B'
    elif cnt_a < cnt_b:
        answer = 'A'
    else:
        answer = '0'

    if (A == 1 or A == P) and (B != 1 and B != P):
        answer = 'A'
    if (B == 1 or B == P) and (A != 1 and A != P):
        answer = 'B'
    if (A == 1 or A == P) and (B == 1 or B == P):
        answer = '0'


    print('#{} {}'.format(tc, answer))
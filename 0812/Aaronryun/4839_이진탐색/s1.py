import sys

sys.stdin = open('input.txt')

T = int(input())


def binary_search(numbers, target):
    low = 1
    high = total

    cnt = 0
    while low <= high:
        cnt += 1

        mid = (low + high) // 2
        if mid == target:
            return cnt

        elif mid > target:

            high = mid
        else:

            low = mid


for test in range(T):
    total, a, b = map(int, input().split())

    A = binary_search(total, a)
    B = binary_search(total, b)

    if A < B:
        print('#{} {}'.format(test + 1, 'A'))
    elif A > B:
        print('#{} {}'.format(test + 1, 'B'))
    else:
        print('#{} {}'.format(test + 1, '0'))

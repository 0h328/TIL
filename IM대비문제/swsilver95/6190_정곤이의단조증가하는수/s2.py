import sys
sys.stdin = open('input.txt')

T = int(input())


def is_uphill(number):
    number = str(number)
    n = len(number)

    for i in range(n - 1):
        if number[i] > number[i + 1]:
            return False

    return True


for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    uphill = -1

    for i in range(N - 1):
        for j in range(i + 1, N):
            num = numbers[i] * numbers[j]
            if is_uphill(num):
                if uphill < num:
                    uphill = num

    print('#{} {}'.format(tc, uphill))
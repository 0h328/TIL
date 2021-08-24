import sys

sys.stdin = open('input.txt')

T = int(input())
for test in range(T):
    N = int(input())

    numbers = list(map(int, input().split()))

    max_data = 0

    for i in range(len(numbers)):
        cnt = 0
        for j in range(i, len(numbers)):
            if numbers[i] > numbers[j]:
                cnt += 1
        if max_data < cnt:
            max_data = cnt

    print('#{} {}'.format(test + 1, max_data))

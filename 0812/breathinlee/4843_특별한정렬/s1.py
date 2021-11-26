import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    l = len(numbers)
    ordered_numbers = sorted(numbers)
    list1 = []

    for i in range(l // 2):
        list1.append(ordered_numbers[-i-1])
        list1.append(ordered_numbers[i])

    print('#{}'.format(tc), end=' ')
    print(*list1[:10])


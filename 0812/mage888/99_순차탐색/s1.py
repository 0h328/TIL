# 정렬된 경우
def ordered_sequential_search(numbers, target):

    n = len(numbers)
    i = 0

    while i < n and numbers[i] < target:
        i += 1

    if i < n and numbers[i] == target:
        return True
    else:
        return False

import sys
sys.stdin = open('input.txt')

numbers = list(map(int, input().split()))
print(ordered_sequential_search(numbers, -9))  # True
print(ordered_sequential_search(numbers, 94))  # False
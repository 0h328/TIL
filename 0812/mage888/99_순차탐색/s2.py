# 정렬되지 않은 경우
def unordered_sequential_search(numbers, target):

    n = len(numbers)
    i = 0

    while i < n and numbers[i] != target:
        i += 1

    if i < n:
        return True
    else:
        return False

import sys
sys.stdin = open('input2.txt')

numbers = list(map(int, input().split()))
print(unordered_sequential_search(numbers, 9))  # True
print(unordered_sequential_search(numbers, 94))  # False
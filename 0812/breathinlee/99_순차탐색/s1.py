import sys
sys.stdin = open("input.txt")

# 정렬되어 있는 경우
def ordered_sequential_search(numbers, target):
    N = len(numbers)
    i = 0
    while i < N and numbers[i] < target:
        i += 1
    if i < N and target == numbers[i]:
        return True
    else:
        return False

numbers = list(map(int, input().split()))
print(ordered_sequential_search(numbers, -9))  # True
print(ordered_sequential_search(numbers, 94))  # False
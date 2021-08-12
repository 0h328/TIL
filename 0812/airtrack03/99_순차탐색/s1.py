import sys
sys.stdin = open('input.txt')

# 정렬된 요소의 순차탐색
# 검색 대상이 리스트 안에 존재하면 True / 아니면 False
def ordered_sequential_search(numbers, target):
    for num in numbers:
        if num == target:
            return True
        if num > target:
            return False
    else:
        return False

numbers = list(map(int, input().split()))
print(ordered_sequential_search(numbers, -9))  # True
print(ordered_sequential_search(numbers, 94))  # False

# 정렬되지 않은 요소의 순차탐색
# 검색 대상이 리스트 안에 존재하면 True / 아니면 False
def unordered_sequential_search(numbers, target):
    for num in numbers:
        if num == target:
            return True
    else:
        return False

numbers = list(map(int, input().split()))
print(unordered_sequential_search(numbers, 9))  # True
print(unordered_sequential_search(numbers, 94))  # False
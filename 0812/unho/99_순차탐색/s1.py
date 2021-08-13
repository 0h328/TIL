import sys
sys.stdin = open('input.txt')

# 정렬된 요소의 순차탐색
# 검색 대상이 리스트 안에 존재하면 True / 아니면 False
def ordered_sequential_search(numbers, target):
    for idx in range(len(numbers)):
        if numbers[idx] > target:
            break
        elif numbers[idx] == target:
            return True

    return False

numbers = list(map(int, input().split()))
print(ordered_sequential_search(numbers, -9))  # True
print(ordered_sequential_search(numbers, 94))  # False
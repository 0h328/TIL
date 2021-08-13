# 정렬된 요소의 순차탐색
# 검색 대상이 리스트 안에 존재하면 True / 아니면 False
def ordered_sequential_search(numbers, target):
    i = 0
    while i < len(numbers) and numbers[i] < target: # 정렬되어있어서 다음 타겟이 두조건을 만족할때 하나씩 보면서 과정을거침
        i += 1

    if i < len(numbers) and numbers[i] == target:  # while문이 종결되었을때 다음 2가지 조건을 확인한다.
            return True

    else:
        return False


def unordered_sequential_search(numbers, target):
    i = 0
    while i < len(numbers) and numbers[i] != target:
        i += 1

    if i < len(numbers) and numbers[i] == target:
        return True
    else:
        return False


    pass
import sys
sys.stdin = open('input.txt')

numbers = list(map(int, input().split()))
numbers_2 = list(map(int, input().split()))
print(ordered_sequential_search(numbers, 8))  # True
print(ordered_sequential_search(numbers, 94))  # False
print(unordered_sequential_search(numbers_2, -9))  # True
print(unordered_sequential_search(numbers_2, 74))
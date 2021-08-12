# 이진 탐색 재귀
import sys
sys.stdin = open('input.txt')


def recursive_binary_search(numbers,low,high, target):
    if low > high:  # 검색 실패
        return False
    else:
        mid = (low + high) // 2
        if target == numbers[mid]:  # 검색성공
            return True
        elif target < numbers[mid]:
            return recursive_binary_search(numbers, low, mid - 1, target)
        elif numbers[mid] < target:
            return recursive_binary_search(numbers, mid + 1, high, target)


numbers = list(map(int, input().split()))
print(recursive_binary_search(numbers, 0, len(numbers)-1, 5)) # True
print(recursive_binary_search(numbers, 0, len(numbers)-1, 10)) # False
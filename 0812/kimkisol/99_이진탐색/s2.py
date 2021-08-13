import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 이진 탐색 재귀

def recursive_binary_search(numbers, left, right, target):
    if left > right:
        return False
    else:
        center = (left + right) // 2
        if target == numbers[center]:
            return True
        elif target < numbers[center]:
            return recursive_binary_search(numbers, left, center-1, target)
        elif target > numbers[center]:
            return recursive_binary_search(numbers, center+1, right, target)

numbers = list(map(int, input().split()))
print(recursive_binary_search(numbers, 0, 9, 5))
print(recursive_binary_search(numbers, 0, 9, 10))

# def recursive_binary_search(numbers, start, end, target):
#     if start > end:
#         return False
#
#     else:
#         middle = (start + end) // 2
#         if target == numbers[middle]:
#             return True
#         elif target < numbers[middle]:
#             return recursive_binary_search(numbers, start, middle - 1, target)
#         elif target > numbers[middle]:
#             return recursive_binary_search(numbers, middle + 1, end, target)
#
# numbers = list(map(int, input().split()))
# print(recursive_binary_search(numbers, 0, 9, 5))
# print(recursive_binary_search(numbers, 0, 9, 10))
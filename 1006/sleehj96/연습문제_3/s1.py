"""
연습 문제3. 이진 탐색
 - 이진 탐색을 반복문과 재귀 함수를 활용하여 구현하시오.
 - 찾고자 하는 값(target)이 있다면 해당 값의 인덱스를 없다면 -1을 반환하시오.
"""

#1. iteration
def binary_search_iteration(target):
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = (start+end) // 2
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1
    return -1


nums = [6, 2, 3, 4, 5, 30, 1, 85, 10, 15, 40]
nums.sort()
target = 2       # 있는 경우 -> 해당 요소의 인덱스 반환
print(binary_search_iteration(target))
target = 90    # 없는 경우 -> -1
print(binary_search_iteration(target))

#2. recursion
def binary_search_recursion(target, start, end):
    mid = (start+end) // 2
    if start <= end:
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return binary_search_recursion(target, mid+1, end)
        else:
            return binary_search_recursion(target, start, mid-1)
    else:
        return -1


nums = [6, 2, 3, 4, 5, 30, 1, 85, 10, 15, 40]
nums.sort()
target = 15       # 있는 경우 -> 해당 요소의 인덱스 반환
print(binary_search_recursion(target, 0, len(nums)-1))
target = 90    # 없는 경우 -> -1
print(binary_search_recursion(target, 0, len(nums)-1))
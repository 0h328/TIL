"""
연습 문제3. 이진 탐색
 - 이진 탐색을 반복문과 재귀 함수를 활용하여 구현하시오.
 - 찾고자 하는 값(target)이 있다면 해당 값의 인덱스를 없다면 -1을 반환하시오.
"""

#1. iteration
def binary_search_iteration(nums, key):
    N = len(nums)
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    else:
        return -1


nums = [6, 2, 3, 4, 5, 30, 1, 85, 10, 15, 40]
nums.sort()
target = 85       # 있는 경우 -> 해당 요소의 인덱스 반환
# target = 90    # 없는 경우 -> -1
print(nums)
print(binary_search_iteration(nums, target))


#2. recursion
def binary_search_recursion(start, end, key):
    mid = (start + end) // 2
    if start > end:
        return -1
    if nums[mid] == key:
        return mid
    elif nums[mid] < key:
        return binary_search_recursion(mid+1, end, key)
    else:
        return binary_search_recursion(start, mid-1, key)

nums = [6, 2, 3, 4, 5, 30, 1, 85, 10, 15, 40]
nums.sort()
target = 2       # 있는 경우 -> 해당 요소의 인덱스 반환
print(binary_search_recursion(0, len(nums)-1, target))
target = 90    # 없는 경우 -> -1
print(binary_search_recursion(0, len(nums)-1, target))
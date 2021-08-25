# 참고 1
# https://ko.wikipedia.org/wiki/%ED%80%B5_%EC%A0%95%EB%A0%AC
def quicksort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2] #
    less = []
    more = []
    equal = []
    for a in nums:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    # return quicksort(less) + equal + quicksort(more)
    return [*quicksort(less), *equal, *quicksort(more)]


import sys
sys.stdin = open('input.txt')
nums = list(map(int, input().split()))
print(quicksort(nums))

# 참고 2 (위의 코드와 거의 방식)
def quick_sort(nums: list) -> list:
    if len(nums) <= 1:                              # 정렬 할 대상의 길이가 1이하인 경우 바로 반환
        return nums
    pivot = nums[0]                                 # 0번째 요소를 pivot으로 선택하고
    left, right = [], []                            # 왼쪽과 오른쪽 리스트를 준비하고
    for i in range(1, len(nums)):                   # 1번째부터 비교 시작 -> (첫 시행 기준으로) left는 pivot보다 작은 / right는 pivot보다 큰 요소들이 모아짐
        if nums[i] > pivot:                         # pivot보다 큰 경우 오른쪽 리스트에
            right.append(nums[i])
        else:                                       # pivot보다 작은 경우 왼쪽 리스트에 추가
            left.append(nums[i])

    sorted_left = quick_sort(left)                  # 왼쪽과 오른쪽 리스트에 대해 재귀적으로 반복작업 수행
    sorted_right = quick_sort(right)
    return [*sorted_left, pivot, *sorted_right]     # 정렬된 리스트 최종 반환

# 가변 배열
import sys
sys.stdin = open('input.txt')
nums = list(map(int, input().split()))
print(quick_sort(nums))
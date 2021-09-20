def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1    # 좌측 pivot
    right = end         # 우측 pivot
    done = False        # pivot들이 겹쳐지는 지점을 나타내는 flag 변수
    while not done:
        while left <= right and arr[left] <= pivot:     # 피벗보다 큰 값을 마날때까지 계속 이동
            left += 1
        while left <= right and pivot <= arr[right]:    # 피벗보다 작은 값을 마날때까지 계속 이동
            right -= 1
        if right < left:                                # 피벗들이 겹쳐지면 루프 끝
            done = True
        else:                                           # pivot 들이 안 겹쳐지면 교환한다
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]     # pivot 의 원래 위치를 잡아준다
    return right


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)   # 좌측 반 검사
        quick_sort(arr, pivot + 1, end)     # 우측 반 검사
    return arr

import sys
sys.stdin = open('input.txt')
nums = list(map(int, input().split()))
print(quick_sort(nums, 0, len(nums)-1))



# def quicksort(nums):
#     if len(nums) <= 1:
#         return nums
#
#     pivot = nums[len(nums) // 2]
#     less = []
#     more = []
#     equal = []
#     for a in nums:
#         if a < pivot:
#             less.append(a)
#         elif a > pivot:
#             more.append(a)
#         else:
#             equal.append(a)
#
#     return quicksort(less) + equal + quicksort(more)
#
# import sys
# sys.stdin = open('input.txt')
# nums = list(map(int, input().split()))

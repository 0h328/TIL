"""
연습 문제2. 정렬 복습 - 정렬2
"""

#4. 병합 정렬
def merge(l, r):
    l_idx, r_idx = 0, 0
    sorted_list = []
    while l_idx < len(l) and r_idx < len(r):
        if l[l_idx] < r[r_idx]:
            sorted_list.append(l[l_idx])
            l_idx += 1
        else:
            sorted_list.append(r[r_idx])
            r_idx += 1
    while l_idx < len(l):
        sorted_list.append(l[l_idx])
        l_idx += 1
    while r_idx < len(r):
        sorted_list.append(r[r_idx])
        r_idx += 1

    return sorted_list


def partition(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    l = partition(left)
    r = partition(right)

    return merge(l, r)

numbers = [0, 55, 22, 33, 2, 1, 10, 26, 42]
print(numbers)               # 정렬 전
print(partition(numbers))    # 정렬 후


#5. 퀵 정렬
def quick_sort(nums, left, right):
    if left < right:
        p = partition(nums, left, right)
        quick_sort(nums, left, p-1)
        quick_sort(nums, p+1, right)


def partition(nums, left, right):
    pivot = nums[left]
    i, j = left, right
    while i <= j:
        while i <= j and nums[i] <= pivot:
            i += 1
        while i <= j and nums[j] >= pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[left], nums[j] = nums[j], nums[left]

    return j

quick_nums = [0, 55, 22, 33, 2, 1, 10, 26, 42]
quick_sort(quick_nums, 0, len(quick_nums)-1)
print(quick_nums)
"""
def merge(left, right):
    sorted_list = []
    l_idx, r_idx = 0, 0

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            sorted_list.append(left[l_idx])
            l_idx += 1
        else:
            sorted_list.append(right[r_idx])
            r_idx += 1

    if l_idx == len(left):
        sorted_list += right[r_idx:]
    else:
        sorted_list += left[l_idx:]

    return sorted_list



def partition(arr):
    if len(arr) < 2:
        return arr

    left = partition(arr[:len(arr)//2])
    right = partition(arr[len(arr)//2:])

    return merge(left, right)


numbers = [0, 55, 22, 33, 2, 1, 10, 26, 42, 10, 11, 12, 13]
print(numbers)               # 정렬 전
print(partition(numbers))    # 정렬 후
"""

# 퀵 정렬
def partition(arr, start, end):
    left = start + 1
    right = end

    while True:
        while left <= right and arr[left] <= arr[start]:
            left += 1
        while left <= right and arr[start] <= arr[right]:
            right -= 1
        
        if right < left:
            break
        arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)
    return arr


quick_nums = [0, 55, 22, 33, 2, 1, 10, 26, 42]

print('정렬 전')
print(quick_nums)

result = quick_sort(quick_nums, 0, len(quick_nums)-1)

print('---------------------------------')
print('정렬 후')
print(result)
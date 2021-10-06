"""
연습 문제2. 정렬 복습 - 정렬2
"""

#4. 병합 정렬
def merge(left, right):
    sorted_list = []
    L = R = 0

    while L < len(left) and R < len(right):
        if left[L] < right[R]:
            sorted_list.append(left[L])
            L += 1
        else:
            sorted_list.append(right[R])
            R += 1
    
    if L == len(left):
        sorted_list += right[R:]
    elif R == len(right):
        sorted_list += left[L:]
    
    return sorted_list

def partition(nums):
    if len(nums) < 2:
        return nums

    left = partition(nums[:len(nums)//2])
    right = partition(nums[len(nums)//2:])

    return merge(left, right)


numbers = [0, 55, 22, 33, 2, 1, 10, 26, 42, 10, 11, 12, 13]
print(numbers)               # 정렬 전
print(partition(numbers))    # 정렬 후


#5. 퀵 정렬
def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)
    return arr

def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1
        
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right

quick_nums = [0, 55, 22, 33, 2, 1, 10, 26, 42]

print('정렬 전')
print(numbers)

result = quick_sort(numbers, 0, len(numbers)-1)

print('---------------------------------')
print('정렬 후')
print(result)
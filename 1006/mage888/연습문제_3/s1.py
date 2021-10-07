"""
연습 문제3. 이진 탐색
 - 이진 탐색을 반복문과 재귀 함수를 활용하여 구현하시오.
 - 찾고자 하는 값(target)이 있다면 해당 값의 인덱스를 없다면 -1을 반환하시오.
"""

#1. iteration
def binary_search_iteration(nums, target, start, end):
    while start <= end:
        mid = start + (end - start) // 2            # 가운데 값을 찾고
        if nums[mid] == target:                     # 값을 찾은 경우
            return mid                              # 해당 인덱스(mid) 반환
        elif nums[mid] < target:                    # target이 더 크면
            start = mid + 1                         # 왼쪽을 버리자 (start를 mid + 1로 이동)
        else:                                       # target이 더 작으면
            end = mid - 1                           # 오른쪽을 버리자 (end를 mid - 1로 이동)
    return -1                                       # 못찾은 경우 -1

nums = [6, 2, 3, 4, 5, 30, 1, 85, 10, 15, 40]
nums.sort()
target = 2       # 있는 경우 -> 있는 값의 인덱스
# target = 90    # 없는 경우 -> -1

start = 0
end = len(nums) - 1
find_val = binary_search_iteration(nums, target, start, end)

if find_val == -1:
    print('{}(은)는 없습니다.'.format(target))
else:
    print('{}(은)는 {}번째에 있습니다.'.format(target, find_val))



######################################################################################################################################################



#2. recursion
def binary_search_recursion(nums, target, start, end):
    if end >= start:
        mid = start + (end - start) // 2
        if nums[mid] == target:                                             # 값을 찾으면 return 하자
            return mid
        elif nums[mid] > target:                                            # 왼쪽에서 찾고
            return binary_search_recursion(nums, target, start, mid-1)      # end를 mid-1로 설정
        else:                                                               # 오른쪽에서 찾자
            return binary_search_recursion(nums, target, mid+1, end)        # start를 mid+1로 설정
    else:
        return -1                                                           # 못찾으면 -1 반환

nums = [6, 2, 3, 4, 5, 30, 1, 85, 10, 15, 40]
nums.sort()
target = 2
# target = 90
start = 0
end = len(nums) - 1

find_val = binary_search_recursion(nums, target, start, end)

if find_val == -1:
    print('{}(은)는 없습니다.'.format(target))
else:
    print('{}(은)는 {}번째에 있습니다.'.format(target, find_val))
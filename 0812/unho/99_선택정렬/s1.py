import sys
sys.stdin = open('input.txt')


def selection_sort(nums):
    for i in range(len(nums)-1):                            # 리스트 맨 앞에서부터 시작
        min_value = nums[i]                                 # 시작하는 수가 제일 작은 값이라고 설정
        min_idx = i                                         # 제일 작은 값의 인덱스
        for j in range(i+1, len(nums)):                     # 시작 인덱스 다음부터 끝까지 순환
            if min_value > nums[j]:                         # 더 작은 값이 나오면 변수에 새로운 값 저장
                min_value = nums[j]
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]     # 현재 인덱스와 제일 작은값을 가진 인덱스의 값 교환

    return nums

numbers = list(map(int, input().split()))
print(numbers)
print(selection_sort(numbers))
def partition(nums, left, right):
    i = left - 1                                     # 피봇보다 큰  구간 왼쪽 경계
    j = left                                         # 피봇 보다 큰 구간 오른쪽 경계
    pivot = nums[right]                              # 가장 오른 쪽 원소를 피봇으로 결정
    while j < right:                                 # 피봇에 다다르기 전까지
        if pivot > nums[j]:                          # 피봇보다 작으면
            i += 1                                   # i 이동
            if i < j:                                # i와 j가 다르면 피봇보다 큰 구간 존재
                nums[i], nums[j] = nums[j], nums[i]  # 교환
        j += 1
    nums[i+1], nums[right] = pivot, nums[i+1]        # 피봇과 교환
    return i+1

def quick_sort(nums, left, right):
    if left < right:                          # 교차 여부 확인
        pivot = partition(nums, left, right)  # pivot 잡고
        quick_sort(nums, left, pivot-1)       # 시작 ~ pivot보다 하나 앞 
        quick_sort(nums, pivot+1, right)      # pivot보다 하나 뒤 ~ 끝

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    quick_sort(nums, 0, N-1)                  # 정렬 할 배열, 시작(0), 끝(N-1)
    print('#{} {}'.format(tc, nums[N//2]))
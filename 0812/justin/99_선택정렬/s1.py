def selection_sort(nums):
    for i in range(len(nums)-1):        # 마지막 요소는 원소가 1개 있으니 정렬 할 필요가 없음
        min_idx = i                     # 최솟값에 해당하는 index를 i부터 시작 (0번 위치가 기준위치) -> 반복을 돌면서 자리가 하나씩 결정
        for j in range(i+1, len(nums)): # i 다음부터 보자 (i부터하면 불필요하게 한번 더 봐야하는 상황이 생김)
            if nums[min_idx] > nums[j]: # 내가 가진 최솟값(min_idx)보다 더 작다? 큰걸 뒤로 보낸다는 느낌으로!
                min_idx = j             # 인덱스 갱신

        nums[i], nums[min_idx] = nums[min_idx], nums[i]  # i번째와 min_idx 위치를 교환 (교환은 마지막에 한번)
        print('기준 자리 : ', i, nums)                    # 확인

import sys
sys.stdin = open('input.txt')
numbers = list(map(int, input().split()))
print('정렬 전: ', *numbers)
print('====================================================================')
selection_sort(numbers)
print('====================================================================')
print('정렬 후: ', *numbers)
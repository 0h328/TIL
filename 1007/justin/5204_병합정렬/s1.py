def solve(nums):
    global ans
    if len(nums) > 1:                  # 종료 조건
        mid = len(nums) // 2           # 중간 인덱스
        left = nums[:mid]              # 왼쪽 / 오른쪽 분할 -> 문제의 조건에 맞춰 분할
        right = nums[mid:]
        solve(left)                    # 왼쪽 & 오른쪽 계속 분할
        solve(right)
        l = r = k = 0                  # 왼 & 오를 컨트롤 하는 인덱스 /  left & right 증가 여부와 상관없이 nums의 인덱스를 맞춰 줄 k

        while l != len(left) and r != len(right):
            if left[l] < right[r]:
                nums[k] = left[l]      # 더 작은 값인 left를 nums의 k번째 자리로
                l += 1                 # l을 하나 올려주고
            else:
                nums[k] = right[r]     # 더 작은 값인 right를 nums의 k번째 자리로
                r += 1
            k += 1                     # left/right에 관계없이 nums의 인덱스를 맞춰주기 위함

        while l < len(left):           # 위에서 right의 자리를 결정했다면
            nums[k] = left[l]          # left의 자리를 최종 결정하자
            l += 1                     # 인덱스도 맞춰주고
            k += 1                     # left & right 증가 여부와 상관없이 nums의 인덱스를 맞춰 줄 k

        while r < len(right):          # 위에서 left의 자리를 결정했다면
            nums[k] = right[r]         # right의 자리를 최종 결정하자
            r += 1                     # 인덱스도 맞춰주고
            k += 1                     # left & right 증가 여부와 상관없이 nums의 인덱스를 맞춰 줄 k

        if left[-1] > right[-1]:       # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 더 큰 경우
            ans += 1

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())                       # 정렬 대상의 요소 수
    nums = list(map(int, input().split())) # 정렬 대상
    ans = 0                                # 분할 과정에서 왼쪽이 더 큰 경우를 체크
    solve(nums)
    print('#{} {} {}'.format(tc, nums[N//2], ans))
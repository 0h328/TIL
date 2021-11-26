def solve(nums):
    global ans

    if len(nums) == 1:                                      # 종료 조건 => 계속 분할 하다가 요소가 1개 남은 순간
        return nums

    mid = len(nums) // 2                                    # 중간값
    left = nums[:mid]                                       # 왼쪽 절반  (배열 복사)
    right = nums[mid:]                                      # 오른쪽 절반(배열 복사)

    left = solve(left)                                      # 왼쪽 절반 정렬 -> base case는 -> 요소가 하나 남는 순간
    right = solve(right)                                    # 오른쪽 절반 정렬 -> base case는 -> 요소가 하나 남는 순간
    left_idx = right_idx = k = 0                            # k는 왼쪽/오른쪽 요소 중 위치가 결정 되었을 때 해당 위치를 잡기 위한 값

    while left_idx < len(left) and right_idx < len(right):  # 좌 우 리스트에서 비교 대상이 남은 경우
        if left[left_idx] < right[right_idx]:               # 오른쪽 요소가 더 크다면
            nums[k] = left[left_idx]                        # 왼쪽 값을 먼저 넣고 (작은 값부터)
            left_idx += 1                                   # 왼쪽 idx 증가
        else:
            nums[k] = right[right_idx]                      # 반대면 오른쪽부터 넣고
            right_idx += 1                                  # 오른쪽 idx 증가
        k += 1                                              # k는 left & right에 상관없이 일정하게 증가

    if left_idx < len(left):                                # (한 쪽만 남은 경우) 왼쪽 리스트가 남은 경우 다 털어 넣고
        nums[k:] = left[left_idx:]
    if right_idx < len(right):                              # (한 쪽만 남은 경우) 오른쪽 리스트가 남은 경우 다 털어 넣자
        nums[k:] = right[right_idx:]
    if left[-1] > right[-1]:                                # 왼쪽 마지막 원소가 오른쪽 마지막 보다 큰 경우 체크
        ans += 1
    return nums                                             # 정렬된 왼쪽과 오른쪽이 합쳐진 최종 요소 반환

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    ans = 0
    result = solve(nums)
    print('#{} {} {}'.format(tc, result[N//2], ans))
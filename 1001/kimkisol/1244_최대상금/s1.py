import sys

sys.stdin = open('input.txt')

# 반드시 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 된다 (같은 숫자끼리의 중복 의미 X)
T = int(input())

for t in range(1, T + 1):
    nums, cnt = input().split() # num: 숫자, cnt: 교환 횟수
    nums = list(nums)
    cnt = int(cnt)
    org_cnt = cnt

    for i in range(len(nums) - 1):
        max_idx = i
        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[max_idx]:
                max_idx = j
        if i != max_idx:
            nums[i], nums[max_idx] = nums[max_idx], nums[i]
            cnt -= 1
        if cnt == 0:
            break

    duplicated_nums = 0
    if org_cnt > len(nums):
        org_cnt = len(nums)
    for i in range(org_cnt - 1):
        if nums[i] == nums[i + 1]:
            duplicated_nums += 1

    for i in range(len(nums) - duplicated_nums - 1, len(nums) - 1):
        for j in range(i, len(nums)):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    if cnt % 2 and len(nums) == len(set(nums)):
        nums[-1], nums[-2] = nums[-2], nums[-1]

    print('#{}'.format(t), ''.join(nums))
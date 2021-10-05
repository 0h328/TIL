import sys

sys.stdin = open('input.txt')

# 반드시 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 된다 (같은 숫자끼리의 중복 의미 X)
T = int(input())

for t in range(1, T + 1):
    nums, cnt = input().split() # nums: 숫자, cnt: 교환 횟수
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

    start, end = -1, -1
    # 구간으로 만들어줘야함 구간은 1개란 가정, 6자리만 가능함
    if org_cnt > 3:
        org_cnt = 3
    for i in range(org_cnt - 1):
        if nums[i] == nums[i + 1]:
            if start == -1:
                start = i
                end = i + 1
            else:
                end = i + 1

    for i in range(len(nums) - end - 1, len(nums) - start):
        for j in range(i, len(nums)):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    if cnt % 2 and len(nums) == len(set(nums)):
        nums[-1], nums[-2] = nums[-2], nums[-1]

    print('#{}'.format(t), ''.join(nums))
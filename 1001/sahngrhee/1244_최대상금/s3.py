import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    num, change = map(int, input().split())
    nums = []
    while num > 0:
        nums = [num % 10] + nums
        num //= 10
    new_nums = list(reversed(sorted(nums)))

    counter = [0] * (max(nums) + 1)
    for num in nums:
        counter[num] += 1

    for i in range(len(nums)):
        temp = nums[i]
        max_idx = i
        lower = 0
        for j in range(i+1, len(nums)):
            if nums[i] <= nums[j]:
                nums[i] = nums[j]
                max_idx = j
        for m in range(i+1, max_idx):
            if temp > nums[m]:
                lower += 1
        if lower != 0:
            for k in range(max_idx-1, i, -1):
                if nums[k] == nums[i]:
                    lower -= 1
                if lower == 0:
                    max_idx = k
                    break
        if max_idx != i and nums[max_idx] != temp:
            nums[max_idx] = temp
            change -= 1
        if nums == new_nums:
            for count in counter:
                if count > 1:
                    break
            else:
                if change % 2:
                    nums[len(nums)-1], nums[len(nums)-2] = nums[len(nums)-2], nums[len(nums)-1]
                    break
        if not change:
            break

    ans = ''.join(map(str, nums))
    print('#{} {}'.format(test_case, ans))







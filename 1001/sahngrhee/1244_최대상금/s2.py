import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    num, cnt = map(int, input().split())
    nums = []
    while num > 0:
        nums = [num % 10] + nums
        num //= 10

    counter = [0] * (max(nums) + 1)
    for i in range(len(nums)):
        counter[nums[i]] += 1

    for i in range(len(nums)):
        temp = nums[i]
        max_idx = i
        lower = 0
        for j in range(i+1, len(nums)):
            if nums[i] <= nums[j]:
                nums[i] = nums[j]
                max_idx = j
            if temp > nums[j]:
                lower += 1
        if lower == 0:
            lower = -1
        for k in range(max_idx-1, i, -1):
            if nums[k] == nums[i]:
                lower -= 1
            if lower == 0:
                max_idx = k
        if max_idx != i and nums[max_idx] != temp:
            nums[max_idx] = temp
            cnt -= 1
        if not cnt:
            break

    ans = ''.join(map(str, nums))
    print('#{} {}'.format(test_case, ans))







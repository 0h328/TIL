import sys
sys.stdin = open('input.txt')

for m in range(10):
    Try = int(input())
    nums = list(map(int,input().split()))
    for i in range(len(nums) - 1, 0, -1):
        for k in range(i):
            if nums[k] > nums[k + 1]:
                nums[k], nums[k + 1] = nums[k + 1], nums[k]
    while Try > 0:
        nums[len(nums)-1] -= 1
        nums[0] += 1
        Try -= 1
        for i in range(len(nums) - 1, 0, -1):
            for k in range(i):
                if nums[k] > nums[k + 1]:
                    nums[k], nums[k + 1] = nums[k + 1], nums[k]
    ans = nums[len(nums)-1]-nums[0]
    print('#{} {}'.format(m+1,ans))


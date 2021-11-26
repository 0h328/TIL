import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for t in range(T):
    nums = list(map(int, input().rstrip()))
    print(nums)
    cnt_nums = [0] * 10
    baby_gin = 0
    for num in nums:
        cnt_nums[num] += 1
    # triplet 3장 동일
    idx = 0
    while idx < len(cnt_nums):
        if cnt_nums[idx] >= 3:
            baby_gin += 1
            cnt_nums[idx] -= 3
            idx -= 1
        idx += 1
    # run 연속된숫자
    idx = 0
    while idx < len(cnt_nums) - 2:
        if cnt_nums[idx] >= 1 and cnt_nums[idx+1] >= 1 and cnt_nums[idx+2] >= 1:
            baby_gin += 1
            cnt_nums[idx] -= 1
            cnt_nums[idx+1] -= 1
            cnt_nums[idx+2] -= 1
            idx -= 1
        idx += 1
    result = 1 if baby_gin == 2 else 0
    print('#{0} {1}'.format(t+1, result))
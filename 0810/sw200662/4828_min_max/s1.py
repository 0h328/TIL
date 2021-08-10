import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(N):
    M = int(input())
    nums = list(map(int,input().split()))
    for a in range(len(nums) - 1, 0, -1): # 버블정렬을 가져옴
        for k in range(a):
            if nums[k] > nums[k + 1]:
                nums[k], nums[k + 1] = nums[k + 1], nums[k]
    ans = nums[M-1] - nums[0] # 거기서 가져온값을 기준으로 맨앞과 맨뒤를 뺌
    print('#{} {}'.format(i+1,ans))

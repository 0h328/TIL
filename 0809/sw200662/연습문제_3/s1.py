import sys
sys.stdin = open('input.txt')

N = int(input())
nums = []
for i in range(N):
    M = int(input())
    nums = list(map(int,input().split()))
    max_gravity = 0
    temp_max_gravity = 0
    for k in range(M):
        count = 0
        max_height = nums[k]
        for t in range(k+1,M):
            if max_height <= nums[t]:
                count += 1
        temp_max_gravity = M - 1 - k - count
        if temp_max_gravity > max_gravity:
            max_gravity = temp_max_gravity
    print('#{} {}'.format(i + 1, max_gravity))
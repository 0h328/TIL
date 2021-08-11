import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for t in range(T):
    input()
    nums = list(map(int, input().split()))
    min_num = max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    print('#{0} {1}'.format(t + 1, max_num - min_num))

import sys
sys.stdin = open('input.txt')
numbers = []

for i in range(10):
    Wid = int(input())
    nums = list(map(int,input().split()))
    count = 0
    for k in range(2,Wid-2):
        new_list=[nums[k-2],nums[k-1],nums[k+1],nums[k+2]]
        max_height = max(new_list)
        if max_height < nums[k]:
            count += (nums[k] - max_height)

    print('#{} {}'.format(i + 1, count))
import sys
sys.stdin = open('input.txt')

T = int(input())

def whythey(nums):
    if len(nums) == 1:
        return nums
    middle = (len(nums)-1)//2 + 1
    left = nums[:middle]
    right = nums[middle:]

    left = whythey(left)
    right = whythey(right)

    return cal(left[0],right[0])

def cal(a,b):
    if card[a] == card[b]:
        return [a]
    elif card[a] == 1:
        if card[b] == 2:
            return [b]
        else:
            return [a]
    elif card[a] == 2:
        if card[b] == 3:
            return [b]
        else:
            return [a]
    elif card[a] == 3:
        if card[b] == 1:
            return [b]
        else:
            return [a]

for i in range(T):
    N = int(input())
    card = list(map(int,input().split()))
    nums = list(range(N))
    print('#{} {}'.format(i+1,whythey(nums)[0]+1))

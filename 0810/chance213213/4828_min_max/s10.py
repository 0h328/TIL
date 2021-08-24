import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    nums = list(map(int, input()))
    ans = nums[0]
    for idx in range(N-1):
        if nums[idx] < nums[idx+1]:
            ans = nums[idx+1]

    print('#{} {}'.format(tc+1, ans))
import sys
sys.stdin = open('input.txt')

T = int(input())

def card(N, nums):
    cnt = [0] * 10
    max_num = 0
    for i in range(len(nums)):
        cnt[nums[i]] += 1

    for j in range(len(cnt)-1, -1, -1):
        if cnt[j] == max(cnt):
            max_num = j
            break

    return max_num, max(cnt)


for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input()))
    ans1, ans2 = card(N, nums)
    print('#{} {} {}'.format(tc, ans1, ans2))

import sys
sys.stdin = open('input.txt')

nums = list(map(int,input().split()))
ans = [0] * len(nums)
cnt = [0] * 17

def countsort(nums,ans,cnt):
    for i in nums:
        cnt[i] += 1
    for k in range(len(cnt)-1):
        cnt[k+1] += cnt[k]
    for c in nums:
        ans[cnt[c]-1] = c
        cnt[c] -=1
    print(ans)


countsort(nums,ans,cnt)
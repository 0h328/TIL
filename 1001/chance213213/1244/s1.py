import sys
sys.stdin = open('input.txt')

def find_idx(nums, i):
    maxi = -1
    mini = 11
    for idx in range(i, len(nums)):
        if nums[idx] >= maxi:
            maxi = nums[idx]
            max_idx = idx
    for idx in range(len(nums)-1, i-1, -1):
        if nums[idx] <= mini:
            mini = nums[idx]
            min_idx = idx
    return max_idx, min_idx


T = int(input())

for tc in range(1, T+1):
    N, K = input().split()
    nums = []
    for n in N:
        nums.append(int(n))
    K = int(K)
    print(nums, K)
    max_N = sorted(nums, reverse=True)
    #sorted는 원래 객체 변화 없음. sort는 원래 리스트도 정렬해 버림
    max_idx, min_idx = find_idx(nums, 0)
    cnt = 0
    if K == 1:
        if nums[max_idx] == nums[0]:
            max_idx, min_idx = find_idx(nums, 1)
        #가장 큰 숫자를 첫째자리로 보내기
        nums[max_idx], nums[0] = nums[0], nums[max_idx]

    print(f'K가 1일때 정렬 결과는 {nums}')

    if K >= 2:
        nums[max_idx], nums[0] = nums[0], nums[max_idx]
        cnt += 1
        for s in range(1, len(nums)):
            if nums[s] == max_N[s]:
                continue
            max_idx, min_idx = find_idx(nums, s)
            nums[max_idx], nums[min_idx] = nums[min_idx], nums[max_idx]
            cnt += 1
            if nums == max_N:
                if (K-cnt)%2==1 and len(set(nums))==len(nums):
                    nums[len(nums)-1], nums[len(nums)-2] = nums[len(nums)-2], nums[len(nums)-1]
                break
            if cnt == K:
                break
    print(f'K가 2이상일 떄 정렬결과는 {nums}')




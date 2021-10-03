import sys

sys.stdin = open('input.txt')


def find_idx(nums, i):
    maxi = -1
    mini = 11
    for idx in range(i, len(nums)):
        if nums[idx] >= maxi:
            maxi = nums[idx]
            max_idx = idx
    for idx in range(len(nums) - 1, i - 1, -1):
        if nums[idx] <= mini:
            mini = nums[idx]
            min_idx = idx
    return max_idx, min_idx

def find_idx2(nums,j):
    maxi = -1
    mini = 11
    for idx in range(j):
        if nums[idx] >= maxi:
            max_idx = idx
    for idx in range(j-1, -1, -1):
        if nums[idx] <= mini:
            mini = nums[idx]
            min_idx = idx

    return max_idx, min_idx


T = int(input())

for tc in range(1, T + 1):
    N, K = input().split()
    nums = []
    for n in N:
        nums.append(int(n))
    K = int(K)
    # print(nums, K)
    max_N = sorted(nums, reverse=True)
    # sorted는 원래 객체 변화 없음. sort는 원래 리스트도 정렬해 버림
    max_idx, min_idx = find_idx(nums, 0)
    cnt = 0
    if K == 1:
        if nums[max_idx] == nums[0]:
            max_idx, min_idx = find_idx(nums, 1)
        # 가장 큰 숫자를 첫째자리로 보내기
        nums[max_idx], nums[0] = nums[0], nums[max_idx]
    max_num = max(nums)
    max_cnt = 0
    for num in nums:
        if num == max_num:
            max_cnt += 1
    max_idx_list = []

    if K >= 2:
        if max_cnt >= 2:
            for s in range(len(nums)):
                if nums[s] == max_N[s]:
                    continue
                max_idx, min_idx = find_idx(nums, s)
                nums[min_idx], nums[max_idx] = nums[max_idx], nums[min_idx]
                cnt += 1
                if cnt == K:
                    break
            # for j in range(len(nums)-1, -1, -1):
            #     max_idx, min_idx = find_idx2(nums, j)
            # for idx in range(len(nums)):
            #     if nums[idx] == max_num:
            #         max_idx_list.append(idx)
            # my_min = 11
            # for idx in range(len(max_idx_list)-1, -1, -1):
            #     for i in range(idx+1, -1, -1):
            #         if nums[i] <= my_min:
            #             my_min = nums[i]
            #             min_idx = i
            #


        for s in range(len(nums)):
            if nums[s] == max_N[s]:
                continue
            max_idx, min_idx = find_idx(nums, s)
            nums[max_idx], nums[s] = nums[s], nums[max_idx]
            cnt += 1
            if nums == max_N:
                if (K - cnt) % 2 == 1 and len(set(nums)) == len(nums):
                    nums[len(nums) - 1], nums[len(nums) - 2] = nums[len(nums) - 2], nums[len(nums) - 1]
                break
            if cnt == K:
                break

    print('#{} '.format(tc), end='')
    for num in nums:
        print(num, end='')
    print()




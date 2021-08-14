import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

#선택정렬
T = int(input())

for t in range(1, T + 1):
    nums_len = int(input())
    nums = list(map(int, input().split()))

    #제일 작은숫자 배치하며 범위를 앞에서 마지막에서 두번째까지 줄여나감
    for front_idx in range(nums_len - 1):
        #제일 작은숫자 idx값은 범위 첫번째 값 idx로 설정
        min_idx = front_idx
        for idx in range(front_idx, nums_len):
            if nums[idx] < nums[min_idx]:
                min_idx = idx
        #print(front_idx, min_idx)
        nums[front_idx], nums[min_idx] = nums[min_idx], nums[front_idx]

    print('#{} '.format(t), end='')
    for num in nums:
        print(num, end=' ')
    print()

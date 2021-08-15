import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

#버블정렬
T = int(input())

for t in range(1, T + 1):
    nums_len = int(input())
    nums = list(map(int, input().split()))

    #뒤에서 하나씩 범위를 줄여줌
    for back_idx in range(nums_len - 1, 0, -1):
        #0~back_idx 범위 안에서 숫자 두개씩 비교
        for idx in range(back_idx):
            if nums[idx] > nums[idx + 1]:
                nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]

    print('#{} '.format(t), end='')
    for num in nums:
        print(num, end=' ')
    print()

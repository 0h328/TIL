import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(0, N-1):
        my_min = i
        my_max = i

        for j in range(i+1, N):
            if nums[my_min] > nums[j]:
                my_min = j

        for k in range(i+1, N):
            if nums[my_max] < nums[k]:
                my_max = k

        if i % 2:
            nums[i], nums[my_min] = nums[my_min], nums[i]
        else:
            nums[i], nums[my_max] = nums[my_max], nums[i]

    ans = nums[0:10]

    print('#{}'.format(test_case), end=' ')
    for num in ans:
        print(num, end=' ')
    print()
import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    def binary_search(numbers, target):
        start = 1
        end = total_page
        cnt = 0
        while True:
            middle = (start + end) // 2
            if numbers[middle] == target:
                cnt += 1
                return cnt
            elif numbers[middle] > target:
                cnt += 1
                end = middle
            else:
                cnt += 1
                start = middle

    total_page, target_A, target_B = map(int, input().split())
    nums = [i for i in range(total_page+1)]

    cnt_A = binary_search(nums, target_A)
    print(cnt_A)
    cnt_B = binary_search(nums, target_B)
    print(cnt_B)
    if cnt_A < cnt_B:
        print('#{} {}'.format(test_case, 'A'))
    elif cnt_A == cnt_B:
        print('#{} {}'.format(test_case, '0'))
    else:
        print('#{} {}'.format(test_case, 'B'))

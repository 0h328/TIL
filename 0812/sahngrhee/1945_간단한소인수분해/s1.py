import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    nums = [2, 3, 5, 7, 11]
    ans = ''

    for num in nums:
        cnt = 0
        while N % num == 0:
            cnt += 1
            N //= num
        ans += str(cnt) + ' '

    print('#{} {}'.format(test_case, ans))


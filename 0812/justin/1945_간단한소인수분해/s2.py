def solve(num):
    prime_nums = [2, 3, 5, 7, 11]
    counter = [0] * 5

    for i in range(len(prime_nums)):
        d = prime_nums[i]
        while not num % d:  # N이 해당 소수로 더 이상 나누어 떨어지지 않을때까지 소수로 나누자
            num //= d       # 몫은 num에 (다시 나눠야 할 값)
            counter[i] += 1 # 해당 소인수는 카운트
    return ' '.join(map(str, counter))

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    num = int(input())
    ans = solve(num)
    print('#{} {}'.format(tc, ans))
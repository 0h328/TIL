import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    prime_nums = [2, 3, 5, 7, 11] # 문제에서 주어진 소수
    cnt = [0] * 5                 # 소수의 개수 체크

    for i in range(len(prime_nums)):
        while N % prime_nums[i] == 0: # 나누어 떨어지면
            cnt[i] += 1               # 해당 소수 cnt
            N //= prime_nums[i]       # 몫을 취한다.
    ans = ' '.join(map(str, cnt))
    print('#{} {}'.format(tc, ans))
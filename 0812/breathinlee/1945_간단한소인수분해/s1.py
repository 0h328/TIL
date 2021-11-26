import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prime_numbers = [2, 3, 5, 7, 11]
    prime_cnt = [0] * 5

    for i in range(5):
        while N % prime_numbers[i] == 0:
            prime_cnt[i] += 1
            N //= prime_numbers[i]

    print('#{}'.format(tc), end=' ')
    print(*prime_cnt)



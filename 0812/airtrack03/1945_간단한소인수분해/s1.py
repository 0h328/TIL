# N이 2, 3, 5, 7, 11의 지수의 곱으로 만들어 질 수 있는 a, b, c, d, e 값 구하는 문제
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    prime_nums = [2, 3, 5, 7, 11]
    result = []     # a, b, c, d, e 저장할 리스트

    for prime_num in prime_nums:    # 소수 리스트의 소수 하나씩 체크
        cnt = 0
        while N % prime_num == 0:   # 소수로 계속 나눠서 소수 곱이 사라지면 나머지가 생기므로 while 종료
            cnt += 1
            N //= prime_num
        result.append(cnt)

    ans = ' '.join(list(map(str, result)))

    print('#{} {}'.format(tc, ans))
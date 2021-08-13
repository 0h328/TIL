import sys
sys.stdin = open('input.txt')



test_case = int(input())

for tc in range(1, test_case+1):
    n = int(input())
    answer = []

    for e in [2, 3, 5, 7, 11]:          # 소인수분해 할 숫자들
        i = 0
        while n % (e**i) == 0:          # 더 나눠지지 않을때까지
            i += 1

        answer.append(i-1)

    print('#{} {} {} {} {} {}'.format(tc, *answer))
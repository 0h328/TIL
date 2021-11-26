import sys
sys.stdin = open('input.txt')

T = int(input())

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, T+1):
    pay = int(input()[:-1] + '0')

    can_pay_list = []

    for i in money:
        can_pay_list.append(pay // i)   # if / else 분기처리 안해줘도 상관 X
        pay = pay - i * (pay // i)      # pay = pay % i

    print(f'#{tc}')
    print(*can_pay_list)
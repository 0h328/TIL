'''
퀴즈 대회에 참가해서 우승을 하게 되면 보너스 상금을 획득할 수 있는 기회를 부여받는다.
우승자는 주어진 숫자판들 중에 두 개를 선택에서 정해진 횟수만큼 서로의 자리를 위치를 교환할 수 있다.

여기서 주의할 것은 반드시 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 된다.
다음과 같은 경우 1회의 교환 횟수가 주어졌을 때 반드시 1회 교환을 수행하므로 결과값은 49가 된다. (94 -> 49, 무조건)

정해진 횟수만큼 숫자판을 교환했을 때 받을 수 있는 가장 큰 금액을 계산해보자.
숫자판의 정보는 정수형 숫자로 주어지고 최대 자릿수는 6자리이며, 최대 교환 횟수는 10번이다.
'''

'''
# 1. 너무 김
# 2. 10개중 5개만 맞음
# 3. Fail (Runtime error)
23:03:26 (Runtime error)
Error Message:
Memory Limit Exceeded
'''

def change_prize(prize, N):
    global i_dont_know_list
    global i_dont_know_list_2
    global result_all

    prize_list = list(prize)

    if N == 0:
        for i in i_dont_know_list:
            answer = ''
            for j in i:
                answer += j
            result_all.append(int(answer))

    else:
        if len(i_dont_know_list) == 0:
            for i in range(len(prize)):
                for j in range(i + 1, len(prize)):
                    result = ''
                    prize_list[i], prize_list[j] = prize_list[j], prize_list[i]
                    for k in prize_list:
                        result += k
                    i_dont_know_list.append(list(result))
                    prize_list = list(prize)
            change_prize(prize, N - 1)


        else:
            for h in i_dont_know_list:
                for i in range(len(prize)):
                    for j in range(i+1, len(prize)):
                        h[i], h[j] = h[j], h[i]
                        i_dont_know_list_2.append(h)
                        h[i], h[j] = h[j], h[i]

            i_dont_know_list = i_dont_know_list_2
            change_prize(prize, N-1)


import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    prize, N = input().split()
    N = int(N)
    i_dont_know_list = []
    i_dont_know_list_2 = []
    result_all = []
    change_prize(prize, N)

    print('#{} {}'.format(tc, max(result_all)))
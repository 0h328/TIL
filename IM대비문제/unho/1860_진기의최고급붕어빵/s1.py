import sys
sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case+1):
    N, M, K = map(int, input().split())     # 명 / 초 / 갯수
    n_list = list(map(int, input().split()))
    n_list.sort()                           # 오름차순
    answer = ''
    sign = False

    remain_bread = 0

    idx = 0
    while n_list:
        if idx%M == 0 and idx != 0:
            remain_bread += K

        while n_list and n_list[0] == idx:
            n_list.pop(0)

            if remain_bread != 0:
                remain_bread -= 1
            elif remain_bread == 0:
                answer = 'Impossible'
                sign = True
                break
        if sign:
            break

        idx += 1

    else:
        answer = 'Possible'

    print('#{} {}'.format(tc, answer))













    # ''' ----------- '''
    # if n_list[0]:
    #     idx = 0                             # 누적
    #     for e in n_list:
    #         tmp_idx = (e//2 - 1) - idx      # 현재 사람의 붕어빵 만든지 몇번째인지
    #         idx = idx + tmp_idx             # 이전과 비교해서 몇번이나 지났는지 차이 값
    #
    #         remain_bread += K * tmp_idx     #
    # else:
    #     answer = 'Impossible'
    #
    # print('#{} {}'.format(tc, answer))

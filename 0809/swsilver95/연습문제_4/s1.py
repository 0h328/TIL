import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    number = list(map(int, input()))
    number_cnt = [0] * 12                       # index 초과를 일으키지 않기 위해 길이를 12로 설정

    for i in range(6):
        number_cnt[number[i]] += 1              # 숫자 카운팅

    tri = 0                                     # tri, run 발생횟수를 카운팅할 변수
    run = 0
    j = 0
    while j < 10:
        if number_cnt[j] >= 3:                  # count가 3이 이상일 경우에 triplet 가능
            number_cnt[j] -= 3
            tri += 1
            continue                            # count가 세 숫자 연속으로 1 이상이면 run 가능
        if number_cnt[j] >= 1 and number_cnt[j+1] >= 1 and number_cnt[j+2] >= 1:
            number_cnt[j] -= 1
            number_cnt[j+1] -= 1
            number_cnt[j+2] -= 1
            run += 1
            continue
        j += 1                                  # 둘 다 없다면 j에 1을 추가해서 while문 계속 동작

    if tri + run == 2:
        print('#{0} {1}'.format(idx, 1))
    else:
        print('#{0} {1}'.format(idx, 0))
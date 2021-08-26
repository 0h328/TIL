import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    numbers = input()
    number_cnt = [0] * 10
    baby_gin = 0

    for number in numbers:
        number_cnt[int(number)] += 1
    # print(number_cnt)
    # triplet
    idx1 = 0
    while idx1 < len(number_cnt):
        if number_cnt[idx1] >= 3:
            baby_gin += 1
            number_cnt[idx1] -= 3
            idx1 -= 1
        idx1 += 1

    # run
    idx2 = 0
    while idx2 < len(number_cnt) - 2:
        if number_cnt[idx2] >= 1 and number_cnt[idx2+1] >= 1 and number_cnt[idx2+2] >= 1:
            baby_gin += 1
            number_cnt[idx2] -= 1
            number_cnt[idx2+1] -= 1
            number_cnt[idx2+2] -= 1
            idx2 -= 1
        idx2 += 1

    if baby_gin == 2:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(tc, result))

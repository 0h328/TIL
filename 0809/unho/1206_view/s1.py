'''
해당 빌딩의 좌우 2개씩을 확인하여 해당 빌딩보다 낮으면 answer 증가
'''

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    number = int(input())
    building_high = list(map(int, input().split()))

    answer = 0

    for i in range(2, number-2):
        tmp1 = tmp2 = tmp3 = tmp4 = 0

        tmp1 = building_high[i] - building_high[i-2]
        tmp2 = building_high[i] - building_high[i-1]
        tmp3 = building_high[i] - building_high[i+1]
        tmp4 = building_high[i] - building_high[i+2]

        if tmp1 > 0 and tmp2 > 0 and tmp3 > 0 and tmp4 > 0:
            answer += min(tmp1, tmp2, tmp3, tmp4)

    print('#{} {}'.format(tc, answer))
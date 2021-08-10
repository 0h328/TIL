'''
1. 리스트에 각 숫자의 갯수를 담는다.
2. 갯수가 3개 이상이면 triplet, 리스트에 갯수가 1개씩 연속적으로 있으면 run


예상 시간복잡도 - O(n)
'''

import sys
sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case+1):
    num = input().strip()               # 숫자를 문자열로 입력받음
    num_list = [0 for _ in range(10)]   # 0~9 의 갯수가 담길 리스트
    answer = 0                          # 정답 여부를 담을 변수
    cnt = 0                             # run or triplet 갯수가 담길 변수


    for n in num:                       # 숫자를 하나씩 가져옴
        idx = int(n) % 10               # 해당 숫자의 인덱스에 갯수를 쌓음
        num_list[idx] += 1

        if num_list[idx] == 3:          # 하나의 숫자가 3개가 되면 triplet 이므로 cnt 변수 1 증가
            num_list[idx] = 0
            cnt += 1

    for idx in range(8):                # 0번부터 3개를 짝을 이루면서 한칸씩 이동
        # 해당 숫자와 다음, 다다음 숫자가 1개씩 있으면 cnt 1 증가 및 값을 0으로 설정
        if num_list[idx] == 1 and num_list[idx + 1] == 1 and num_list[idx + 2] == 1:
            cnt += 1
            num_list[idx], num_list[idx + 1], num_list[idx + 2] = 0, 0, 0

        # 해당 숫자와 다음, 다다음 숫자가 2개씩 있으면 cnt 2 증가
        elif num_list[idx] == 2 and num_list[idx + 1] == 2 and num_list[idx + 2] == 2:
            cnt += 2

    # run or triplet 이 합쳐서 두개이면 answer = 1
    if cnt == 2:
        answer = 1

    print('#{} {}'.format(tc, answer))
'''
숫자가 적힌 카드를 입력받는다
0~9 크기의 리스트를 만들어 각 숫자의 갯수를 카운트 한다.
가장 값이 큰 인덱스가 카드 숫자, 인덱스의 값이 나온 갯수
'''


import sys
sys.stdin = open("input.txt")

test_case = int(input())

for tc in range(1, test_case+1):
    num = int(input())
    cards = input()
    cnt_list = [0] * 10                         # 0~9 까지 숫자의 갯수를 입력할 리스트

    while cards:                                # 카드 숫자의 갯수를 증가
        cnt_list[int(cards[-1])] += 1
        cards = cards[:-1]

    max_card = 0                                # 최대 갯수 0개로 임의 설정
    max_card_idx = 0                            # 최대 갯수가 있는 인덱스 값
    for idx in range(len(cnt_list)):
        if max_card <= cnt_list[idx]:           # 더 크거나 같은 값이 있으면
            max_card = cnt_list[idx]
            max_card_idx = idx


    print('#{} {} {}'.format(tc, max_card_idx, max_card))
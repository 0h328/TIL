# 문제 푼 시간 : 8:33
# 문제 생각 흐름 :
# 혼자서 풀었는가 ?

import sys
sys.stdin = open('input.txt')
# 이제 나는 import sys 장인

def game(A, B): # game는 card_num을 이용해야 함!
    pick_A, pick_B = card_num[A - 1], card_num[B - 1]
    if pick_A - pick_B == -1 or pick_A - pick_B == 2: # B가 이겼을 때
        return B
    else: # A가 이기거나 무승부일 때
        return A


def matching(start, end): # matching은 학생 번호를 이용

    if start == end:
        return start

    left = matching(start, (start+end) // 2)
    right = matching((start+end) // 2 + 1, end)
    # print(left, right)
    return game(left, right)

# 사다리 게임 왜 지겹니 제발 지겹지 않으면 안되겠니..?
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card_num = list(map(int, input().split())) # 이정도는 껌이지
    # print(card_num) # 1: 가위, 2:바위, 3: 보

    result = matching(1, N)
    print('#{} {}'.format(tc, result))


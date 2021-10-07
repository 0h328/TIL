def solve():
    player1_cards = [0 for _ in range(10)]      # player 1
    player2_cards = [0 for _ in range(10)]      # player 2

    for idx in range(12):                                                 # 카드의 수만큼 반복을 돌면서
        n = cards[idx]                                                    # 해당 카드를 넣고
        if idx % 2 == 0:                                                  # 짝수 -> player1
            player1_cards[n] += 1                                         # idx 하나 증가시키고
            # 카드 6장을 모두 가져가지 않더라도 먼저 run or triplet이면 승리
            if player1_cards[n] == 3:                                     # 해당 위치의 카드가 3개 이상이면 == triplet이면 -> player1 승리
                return 1
            if check_run(player1_cards) == 1:                             # run이면 -> player1 승리
                return 1
        else:                                                             # 홀수 -> player2
            player2_cards[n] += 1
            # 카드 6장을 모두 가져가지 않더라도 먼저 run or triplet이면 승리
            if player2_cards[n] == 3:                                     # 해당 위치의 카드가 3개 이상이면 == triplet이면 -> player2 승리
                return 2
            if check_run(player2_cards) == 1:                             # run이면 -> player2 승리
                return 2
    return 0                                                              # return 안만났다면 12개의 카드를 도는 동안 승부를 내지 못했기 때문에 무승부

def check_run(card):
    for i in range(8):                                                    # 인덱스 에러를 피하기 위해 8(n-1 -> 7) -> 0 ~ 9까지의 숫자 카드 중에서 최대 7 + 2 -> 9 (마지막 인덱스 9)
        if card[i] >= 1 and card[i+1] >= 1 and card[i+2] >= 1:            # 연속된 수가 1이상 체크되어있다면 run
            return 1

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))                               # 12장의 카드 목록
    ans = solve()
    print('#{} {}'.format(tc, ans))
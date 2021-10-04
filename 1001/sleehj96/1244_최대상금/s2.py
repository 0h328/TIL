import sys
sys.stdin = open('input.txt')

# 테스트 케이스 9개

def card_sum(cards):
    result = 0
    for card in cards:
        result *= 10
        result += card
    return result


def change(start_idx, d):   # depth
    global max_ans

    if d == k:
        cards_val = card_sum(cards)

        if max_ans < cards_val:
            max_ans = cards_val
        return

    for i in range(start_idx, N-1):
        for j in range(i+1, N):
            if cards[i] <= cards[j]:
                cards[j], cards[i] = cards[i], cards[j]
                change(i, d+1)
                cards[i], cards[j] = cards[j], cards[i]


for T in range(int(input())):
    cards, k = input().split()  # 숫자판 정보, 최대 교환 횟수
    cards = list(map(int, cards))   # 숫자판 정보 정리
    k = int(k)
    N = len(cards)

    max_ans = card_sum(cards)

    if N == 2 or cards == sorted(cards, reverse=True):

        if k & 1:
            cards[-1], cards[-2] = cards[-2], cards[-1]
            max_ans = card_sum(cards)

    else:
        change(0, 0)    # depth=교환 횟수, curr_idx

    print('#{} {}'.format((T+1), max_ans))
    # break

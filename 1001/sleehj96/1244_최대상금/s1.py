import sys
sys.stdin = open('input.txt')


def change(d, start_i):   # depth
    global max_ans

    if d == k or d == N:
        cards_val = 0
        for card in cards:
            cards_val *= 10
            cards_val += card

        if max_ans < cards_val:
            max_ans = cards_val
        return

    # if cards[curr_idx] == max(cards[curr_idx:]):
    #     curr_idx += 1

    for i in range(start_i, N-1):
        for j in range(i+1, N):
            cards[j], cards[i] = cards[i], cards[j]
            change(d+1, i)
            cards[i], cards[j] = cards[j], cards[i]


for T in range(int(input())):
    cards, k = map(int, input().split())    # 숫자판 정보, 최대 교환 횟수
    cards = list(map(int, str(cards)))      # 숫자판 정보 정리
    N = len(cards)

    max_ans = 0
    change(0, 0)    # depth=교환 횟수, curr_idx

    print('#{} {}'.format((T+1), max_ans))
    # break

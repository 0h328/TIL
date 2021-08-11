import sys

sys.stdin = open('input.txt')

t = int(input())

i = 1
while i <= t:

    card_len = int(input())
    num_string = int(input())
    cards = []

    # print(int(input()))
    # print(list(map(int, list(input()))))
    # print(list(map(int, input())))

    for _ in range(card_len):
        cards.append(num_string % 10)
        num_string //= 10

    cards.sort()

    cnt = 1
    the_card = cards[0]

    for card in cards:
        tmp_cnt = cards.count(card)

        if cnt <= tmp_cnt:
            cnt = tmp_cnt
            the_card = card

    print('#{0} {1} {2}'.format(i, the_card, cnt))
    i += 1

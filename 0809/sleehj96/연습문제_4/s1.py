import sys

sys.stdin = open('input.txt')

n = int(input())


def is_baby_gin(cards):
    cards.sort()

    for _ in range(2):      # 666777
        if cards and not cards.count(cards[0]) % 3: # 333333
            for _ in range(cards.count(cards[0])):
                cards.remove(cards[0])

    idx = 0
    while idx < len(cards):
        val = cards[idx]

        if (val + 1) in cards:
            if (val + 2) in cards:
                cards.remove(val)
                cards.remove(val + 1)
                cards.remove(val + 2)
                continue

        idx += 1

    if cards:
        return False
    else:
        return True

i = 1

while i <= n:
    cards_list = list(map(int, input()))

    if is_baby_gin(cards_list):
        ans = 1
    else:
        ans = 0

    print('#{0} {1}'.format(i, ans))

    i += 1
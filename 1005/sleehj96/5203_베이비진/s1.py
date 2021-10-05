import sys
sys.stdin = open('input.txt')


def is_baby_gin(lst: list):
    return is_run(lst) or is_triplet(lst)


def is_run(lst: list):

    for idx in range(10):
        if lst[idx] == 3:
            return 1
    return 0


def is_triplet(lst: list):

    for idx in range(8):
        if all(lst[idx:idx+3]):
            return 1
    return 0


for tc in range(int(input())):
    cards = list(map(int, input().split()))
    A_cards = [0 for _ in range(10)]
    B_cards = [0 for _ in range(10)]

    ans = 0
    for i in range(0, 12, 2):
        if ans:
            break

        A_cards[cards[i]] += 1
        if i >= 4:
            if is_baby_gin(A_cards):
                ans = 1
                break

        B_cards[cards[i+1]] += 1
        if i >= 4:
            if is_baby_gin(B_cards):
                ans = 2
                break

    print('#{0} {1}'.format(tc+1, ans))
    # break

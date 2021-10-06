import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cards = int(''.join(input().split()))

    p1_card_idx = [0] * 12
    p2_card_idx = [0] * 12

    res = 0
    while cards > 0:
        p2_card_idx[cards % 10] += 1
        cards //= 10
        p1_card_idx[cards % 10] += 1
        cards //= 10

        for i in range(9):
            if p1_card_idx[i] >= 3:
                res = 1
                break
            elif p1_card_idx[i] >= 1 and p1_card_idx[i+1] >= 1 and p1_card_idx[i+2] >= 1:
                res = 1
                break

            if p2_card_idx[i] >= 3:
                res = 2
                break
            elif p2_card_idx[i] >= 1 and p2_card_idx[i+1] >= 1 and p2_card_idx[i+2] >= 1:
                res = 2
                break
        if res:
            break

    print('#{} {}'.format(tc, res))
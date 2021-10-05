import sys
sys.stdin = open('input.txt')


def chk_triplet(cnt):
    for i in range(len(cnt)):
        if cnt[i] >= 3:
            return True
    return False


def chk_run(cnt):
    for i in range(len(cnt)-2):
        if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
            return True
    return False


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    p1 = []
    p2 = []
    cnt1 = [0] * 10
    cnt2 = [0] * 10
    winner = 0
    while card:
        p1.append(card.pop(0))
        # [9, 5, 5, 1, 4, 2]
        cnt1[p1[-1]] += 1
        # triplet이나 run있는지 체크
        if chk_triplet(cnt1) or chk_run(cnt1):
            winner = 1
            break
        p2.append(card.pop(0))
        # [9, 6, 6, 1, 2, 1]
        cnt2[p2[-1]] += 1
        # triplet이나 run있는지 체크
        if chk_triplet(cnt2) or chk_run(cnt2):
            winner = 2
            break
    print('#{} {}'.format(tc, winner))



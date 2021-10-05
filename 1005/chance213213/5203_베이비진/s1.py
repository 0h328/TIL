import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    player1 = []
    player1_cnt = [0] * 10
    player2 = []
    player2_cnt = [0] * 10
    result = 0
    for i in range(0, len(cards), 2):
        player1.append(cards[i])
        player1_cnt[cards[i]] += 1
        if 3 in player1_cnt:
            result = 1
            break
        for idx in range(len(player1)-2):
            if player1_cnt[idx] >= 1 and player1_cnt[idx+1] >= 1 and player1_cnt[idx+2] >= 1:
                result = 1
                break
        player2.append(cards[i+1])
        player2_cnt[cards[i+1]] += 1
        if 3 in player2_cnt:
            result = 2
            break
        for idx in range(len(player2)-2):
            if player2_cnt[idx] >= 1 and player2_cnt[idx+1] >= 1 and player2_cnt[idx+2] >= 1:
                result = 2
                break

    print('#{} {}'.format(tc, result))
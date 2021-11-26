import sys
sys.stdin = open('input.txt')

# 테스트케이스 8개 통과..

def is_babygin(player_cnt, numbers):
    cnt = 0
    idx1 = 0
    while idx1 < len(numbers):
        if player_cnt[idx1] >= 3:
            cnt += 1
            player_cnt[idx1] -= 3
            idx1 -= 1
        idx1 += 1

    idx2 = 0
    while idx2 < len(numbers) - 2:
        if player_cnt[idx2] >= 1 and player_cnt[idx2 + 1] >= 1 and player_cnt[idx2 + 2] >= 1:
            cnt += 1
            player_cnt[idx2] -= 1
            player_cnt[idx2 + 1] -= 1
            player_cnt[idx2 + 2] -= 1
            idx2 -= 1
        idx2 += 1

    return cnt


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []
    player1_cnt = [0] * 10
    player2_cnt = [0] * 10

    for i in range(12):
        if i % 2:
            player2.append(cards[i])
        else:
            player1.append(cards[i])

    for number in player1:
        player1_cnt[number] += 1
    for number in player2:
        player2_cnt[number] += 1


    ans1 = is_babygin(player1_cnt, player1)
    ans2 = is_babygin(player2_cnt, player2)

    if ans1 > ans2:
        result = 1
    elif ans1 < ans2:
        result = 2
    else:
        result = 0

    print('#{} {}'.format(tc, result))






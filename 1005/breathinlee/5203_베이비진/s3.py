import sys
sys.stdin = open('input.txt')

# 미완성

def is_babygin(player_cnt):
    if 3 in player_cnt:
        return True

    for j in range(len(player_cnt)-3):
        if player_cnt[j] and player_cnt[j+1] and player_cnt[j+2]:
            return True

    return False

T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    player1_cnt = [0] * 10
    player2_cnt = [0] * 10
    result = 0

    for i in range(6):
        if i % 2:
            player2_cnt[cards[i]] += 1
        else:
            player1_cnt[cards[i]] += 1

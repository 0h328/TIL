import sys
sys.stdin = open('input.txt')

# 테스트케이스 9개 통과...

T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    player1_cnt = [0] * 10
    player2_cnt = [0] * 10
    result = 0

    for i in range(12):
        if i % 2:
            player2_cnt[cards[i]] += 1
        else:
            player1_cnt[cards[i]] += 1

        if 3 in player2_cnt:
            result = 2
            break
        for idx in range(8):
            if player2_cnt[idx] and player2_cnt[idx + 1] and player2_cnt[idx + 2]:
                result = 2
                break
            else:
                continue

        if 3 in player1_cnt:
            result = 1
            break
        for idx in range(8):
            if player1_cnt[idx] and player1_cnt[idx + 1] and player1_cnt[idx + 2]:
                result = 1
                break
            else:
                continue



    print('#{} {}'.format(tc, result))

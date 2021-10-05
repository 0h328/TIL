import sys

sys.stdin = open('input.txt')

T = int(input())


def test_baby_gin(a):
    global player_1_win, player_2_win
    for k in a:
        baby_list[k] += 1

    for z in baby_list:
        if z == 3:
            if i % 2 == 0:
                player_1_win = 1
            else:
                player_2_win = 1
            return
    for z in range(len(baby_list)):
        if z <= 7:
            if baby_list[z] >= 1 and baby_list[z+1] >= 1 and baby_list[z+2] >= 1:
                if i % 2 == 0:
                    player_1_win = 1
                else:
                    player_2_win = 1
                return
for tc in range(1, T + 1):
    card_list = list(map(int, input().split()))
    player_1 = []
    player_2 = []
    player_1_win = 0
    player_2_win = 0
    for i in range(len(card_list)):
        if player_1_win == 1 or player_2_win == 1:
            break
        baby_list = [0] * 10
        if i % 2 == 0:
            player_1.append(card_list[i])
        else:
            player_2.append(card_list[i])

        if i >= 4:
            if i % 2 == 0:
                test_baby_gin(player_1)
            else:
                test_baby_gin(player_2)
    if player_1_win == 0 and player_2_win == 0:
        print('#{} {}'.format(tc,0))
    elif player_1_win == 1:
        print('#{} {}'.format(tc,1))
    else:
        print('#{} {}'.format(tc,2))
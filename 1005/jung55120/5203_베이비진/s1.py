import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    for i in range(6):
        player1[cards[2*i]] += 1
        player2[cards[2*i+1]] += 1
        if i >= 3:
            for j in range(7):
                if player1[j] >= 1 and player1[j+1] >= 1 and player1[j+2] >= 1:
                    print('#{} {}'.format(tc, 1))
                    break
                elif player2[j] >= 1 and player2[j+1] >= 1 and player2[j+2] >= 1:
                    print('#{} {}'.format(tc, 2))
                    break
            for k in range(10):
                if player1[k] == 3:
                    print('#{} {}'.format(tc, 1))
                    break
                elif player2[k] == 3:
                    print('#{} {}'.format(tc, 2))
    else:
        print('#{} {}'.format(tc, 0))
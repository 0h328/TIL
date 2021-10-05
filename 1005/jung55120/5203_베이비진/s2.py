# 테스트 케이스 8개만 맞았다. 이유가 뭘까?

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    result = 0
    for i in range(6):
        player1[cards[2*i]] += 1
        player2[cards[2*i+1]] += 1
        if i >= 2:
            for j in range(7):
                if player1[j] >= 1 and player1[j+1] >= 1 and player1[j+2] >= 1:
                    result += 1
                elif player2[j] >= 1 and player2[j+1] >= 1 and player2[j+2] >= 1:
                    result += 2
                elif result > 0:
                    break

            for k in range(10):
                if player1[k] == 3:
                    result += 1
                    break
                elif player2[k] == 3:
                    result += 2
                elif result > 0:
                    break
    else:
        if result >= 3:
            print('#{} {}'.format(tc, 0))
        else:
            print('#{} {}'.format(tc, result))
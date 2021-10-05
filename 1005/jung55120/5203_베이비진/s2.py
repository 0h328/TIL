# 테스트 케이스 9개만 맞았다. 이유가 뭘까?

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    result = []
    for i in range(6):
        player1[cards[2*i]] += 1
        player2[cards[2*i+1]] += 1
        if i >= 2:
            for j in range(8):
                if player1[j] >= 1 and player1[j+1] >= 1 and player1[j+2] >= 1:
                    result.append(1)
                    break
                if player2[j] >= 1 and player2[j+1] >= 1 and player2[j+2] >= 1:
                    result.append(2)
                    break
                # if result > 0:
                #     break
            for k in range(10):
                if player1[k] == 3:
                    result.append(1)
                    break
                if player2[k] == 3:
                    result.append(2)
                    break
        if result:
            break
    if not result:
        print('#{} {}'.format(tc, 0))
    elif 1 in result:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 2))
        # if result >= 3:
        #     print('#{} {}'.format(tc, 0))
        # else:
        #     print('#{} {}'.format(tc, result))
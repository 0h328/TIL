import sys
sys.stdin = open('input.txt')

def is_babygin(players):
    cnt_numbers = [0] * 10
    for number in players:
        cnt_numbers[number] += 1

    if 3 in cnt_numbers:
        return True

    for j in range(8):
        if cnt_numbers[j] and cnt_numbers[j + 1] and cnt_numbers[j + 2]:
            return True

    return False

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []
    result = 0

    for i in range(12):
        if i % 2:
            player2.append(cards[i])
            if len(player2) >= 3 and is_babygin(player2):
                result = 2
                break
        else:
            player1.append(cards[i])
            if len(player1) >= 3 and is_babygin(player1):
                result = 1
                break

    print('#{} {}'.format(tc, result))

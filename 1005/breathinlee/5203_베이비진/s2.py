import sys
sys.stdin = open('input.txt')

# 테스트케이스 8개 통과...

def is_babygin(numbers):
    cnt_numbers = [0] * 10
    for number in numbers:
        cnt_numbers[number] += 1

    if 3 in cnt_numbers:
        return True

    for j in range(len(cnt_numbers) - 2):
        if cnt_numbers[j] and cnt_numbers[j + 1] and cnt_numbers[j + 2]:
            return True

    return False


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []
    player1_cnt = []
    player2_cnt = []
    result = 0

    for i in range(12):
        if i % 2:
            player2.append(cards[i])
        else:
            player1.append(cards[i])

    for j in range(4):
        if is_babygin(player1[:j+3]):
            result = 1
        if is_babygin(player2[:j+3]):
            result = 2


    print('#{} {}'.format(tc, result))


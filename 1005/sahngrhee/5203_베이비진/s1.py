import sys
sys.stdin = open('input.txt')


def baby_gin(nums):
    counter = [0] * 10
    for num in nums:
        counter[num] += 1

    for i in range(10):
        if counter[i] >= 3:
            return True

    for i in range(8):
        if counter[i] >= 1 and counter[i+1] >= 1 and counter[i+2] >= 1:
            return True

    return False


T = int(input())

for test_case in range(1, T+1):
    cards = list(map(int, input().split()))
    N = len(cards)
    player1 = []
    player2 = []
    cnt = 0
    ans = 0

    while cnt < 12:
        if cnt % 2:
            player2.append(cards[cnt])
            if baby_gin(player2):
                ans = 2
                break
        else:
            player1.append(cards[cnt])
            if baby_gin(player1):
                ans = 1
                break
        cnt += 1

    print('#{} {}'.format(test_case, ans))

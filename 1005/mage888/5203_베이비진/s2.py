import sys
sys.stdin = open('input.txt')

def baby_gin(player):

    for i in range(10):
        if player[i] == 3:  # triplet이 나온 경우
            return 1

    for i in range(8):
        if player[i] >= 1 and player[i+1] >= 1 and player[i+2] >= 1:    # run이 나온 경우
            return 1

    return 0

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    p1 = [0] * 10   # idx를 맞추기 위한 설정
    p2 = [0] * 10

    res = 0

    for i in range(12):
        if i % 2:   # 홀수 -> p2
            p2[cards[i]] += 1
            if baby_gin(p2):
                res = 2
                break
        else:       # 짝수 -> p2
            p1[cards[i]] += 1
            if baby_gin(p1):
                res = 1
                break

    print('#{} {}'.format(tc, res))



import sys

sys.stdin = open('input.txt')

def check(player):
    for i in range(len(player)): # run check
        if player[i] == 3:
            return True

    for j in range(len(player) - 2): # triplet check
        if player[j] and player[j + 1] and player[j + 2]:
            return True
    return False


for test in range(1, 1 + int(input())):
    data = list(map(int, input().split()))
    answer = 0
    p1 = [0] * 10 # 카드의 번호수 만큼 초기화
    p2 = [0] * 10
    for i in range(len(data)):
        if not i & 1:
            p1[data[i]] += 1 # 해당 번호 수의 카드 증가
            if check(p1):
                answer = 1
                break
        else:
            p2[data[i]] += 1
            if check(p2):
                answer = 2
                break

    print('#{} {}'.format(test, answer))

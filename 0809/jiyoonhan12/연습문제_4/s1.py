import sys
sys.stdin = open('input.txt')

def baby_gin(cards):
    result = 0
    counting = [0] * 10 # 0부터 9까지의 counting 정렬 리스트

    for i in cards:
        counting[i] += 1

    cnt = 0
    while cnt < 8:
        if counting[cnt] >= 3: # triplet 검사
            counting[cnt] -= 3
            result += 1
            continue

        if counting[cnt] >= 1 and counting[cnt + 1] >= 1 and counting[cnt + 2] >= 1: # run 검사
            counting[cnt] -= 1
            counting[cnt + 1] -= 1
            counting[cnt + 2] -= 1
            result += 1
            continue

        cnt += 1

    return 1 if result == 2 else 0

T = int(input())

for t in range(T):
    cards = list(map(int, input()))
    print(baby_gin(cards))

    # 3:3으로 나누는 모든 조합 (이거 어떻게 함?!) 여기서 막혀서 아무것도 못했어요...
    # for card in cards:

    # 거기서 run 하고 triplet 검사
    # 둘 다 해당하면 1, 하나라도 아니면 0 return


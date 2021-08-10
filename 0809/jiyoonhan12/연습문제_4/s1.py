import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    cards = list(map(int, input()))
    print(cards)

    # 3:3으로 나누는 모든 조합 (이거 어떻게 함?!) 여기서 막혀서 아무것도 못했어요...
    # for card in cards:

    # 거기서 run 하고 triplet 검사
    # 둘 다 해당하면 1, 하나라도 아니면 0 return


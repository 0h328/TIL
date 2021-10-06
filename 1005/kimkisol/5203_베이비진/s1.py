import sys

sys.stdin = open('input.txt')

'''
1. 0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때
2. 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet
3. 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자
4. 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져감
5. 무승부인 경우 0을 출력
'''


def is_babygin():
    pass

T = int(input())

for t in range(1, T + 1):
    cards = list(map(int, input().split()))
    cards_set = [[0] * 10 for _ in range(3)]
    result = 0

    for i in range(12):
        card = cards[i]
        player = 2 if i % 2 else 1
        cards_set[player][card] += 1
        # triplet 인 경우
        if cards_set[player][card] == 3:
            result = player
            break
        # 해당 카드 기준으로 왼쪽 (X X card)
        if card > 1 and cards_set[player][card - 1] > 0 and cards_set[player][card - 2] > 0:
            result = player
            break
        # 해당 카드 기준으로 오른쪽 (card X X)
        if card < 8 and cards_set[player][card + 1] > 0 and cards_set[player][card + 2] > 0:
            result = player
            break
        # 해당 카드 기준으로 양 옆 (X card X)
        if 0 < card < 9 and cards_set[player][card - 1] > 0 and cards_set[player][card + 1] > 0:
            result = player
            break

    print('#{} {}'.format(t, result))
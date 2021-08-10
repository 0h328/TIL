# Edge case 미처리

def solve(cards):
    counter = [0 for _ in range(10)]  # 카드를 카운트하기 위한 리스트
    is_babygin = 0                    # babygin 임을 판단

    for card in cards:                # 카드 개수 카운트(카운트 정렬과 유사한 방식)
        counter[card] += 1

    for idx in range(len(counter)):
        if counter[idx] >= 3:         # 동일한 카드가 3장 이상 있으면 triplet
            is_babygin += 1           # babygin 카운트
            counter[idx] -= 3         # 가지고 있는 카드 3장을 지우고

        if idx < len(counter) - 2:    # 마지막에서 두번째 직전까지 확인(연속적인 번호 확인)
            if counter[idx] and counter[idx+1] and counter[idx+2]: # 연속한 수가 존재하면
                counter[idx] -= 1                                  # 각 카드 제거
                counter[idx+1] -= 1
                counter[idx+2] -= 1
                is_babygin += 1                                    # babygin 카운트

        if is_babygin == 2:                                        # 카운트가 2가 되면 babygin
            return 1
    return 0                                                       # 2가 아닌 경우는 babygin x


import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input()))
    ans = solve(cards)
    print('#{} {}'.format(tc, ans))
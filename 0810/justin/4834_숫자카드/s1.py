import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    card_count = int(input())       # 카드 수
    cards = list(map(int, input())) # 카드 목록
    counters = [0 for _ in range(10)]   # index와 카드의 숫자를 동일하게 맞춤 (ex. 0 ~ 9까지의 카드 -> 0을 총 10개)
    # print(counters)

    for card in cards:      # 입력 받은 카드를 반복을 돌며
        counters[card] += 1 # 그 수를 카운트
    # print(counters)
    max_idx = idx = 0       # 변수 초기화

    while idx < len(counters):  # counters의 크기보다 작을 때까지 반복을 돌며 (idx -> 10이 되는 순간 index out of range)
        # 만약 idx에 해당하는 카드의 수가 max_idx의 카드 수보다 많을 경우
        # 왜 >= 일까? -> 7짜리 카드 2장 vs 8짜리 카드 2장 -> 8자리 카드여야 하기 때문
        if counters[idx] >= counters[max_idx]:
            max_idx = idx      # index 교체
        # idx 증가
        idx += 1
    print('#{} {} {}'.format(tc, max_idx, counters[max_idx]))

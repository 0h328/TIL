import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    h_cnt = [0] * 101  # 높이 카운트 -> 100이라는 높이까지 이용할 것이라 101까지 생성
    min_value = 100    # box의 index 자체를 값으로 활용
    max_value = 1

    for i in range(100):         # 박스의 높이를 카운트 하면서(h_cnt) 최고점과 최저점을 찾기 (min & max는 최고 & 최저점을 의미)
        h_cnt[boxes[i]] += 1     # 해당 값을 index로 활용 (h_cnt 자리에 boxes의 i번째를 1 증가)
        if boxes[i] > max_value: # min & max 갱신
            max_value = boxes[i]
        if boxes[i] < min_value:
            min_value = boxes[i]

    while N > 0 and min_value < max_value - 1: # 횟수가 남았음에도 평탄화가 이미 끝난 경우 (덤프 횟수가 남아 있으면서 차이가 1이 안나는 경우)
        h_cnt[min_value] -= 1
        h_cnt[min_value+1] += 1

        h_cnt[max_value] -= 1
        h_cnt[max_value-1] += 1

        if h_cnt[min_value] == 0: # 포인터의 이동(변경) -> 작은 값을 다음으로
            min_value += 1

        if h_cnt[max_value] == 0: # 포인트의 이동(변경) -> 큰 값을 이전으로
            max_value -= 1

        N -= 1 # 덤프 줄이기

    ans = max_value - min_value
    print('#{} {}'.format(tc, ans))
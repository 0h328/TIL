import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1, t+1):
    n, m = map(int, input().split())
    cheese = list(map(int, input().split()))    # 인덱스는 피자번호, 값은 피자의 남은 치즈량
    oven = [i for i in range(n)]                # 피자번호를 요소로 가지는 리스트
    cheese_idx, oven_idx = n, 0                 # cheese_idx는 다음 피자번호, oven_idx는 오븐의 입구에 있는 피자번호
    cnt = 0                                     # 다구워진 피자의 수
    while True:
        if oven[oven_idx] != -1:                # oven_idx위치가 비어 있지 않으면 아래 코드 수행(oven_idx위치가 비어있으면 -1)
            cheese[oven[oven_idx]] //= 2
            if cheese[oven[oven_idx]] == 0:
                cnt += 1
                if cheese_idx < m:
                    oven[oven_idx] = cheese_idx
                    cheese_idx += 1
                else:
                    if cnt == m:
                        break
                    oven[oven_idx] = -1
        oven_idx = (oven_idx + 1) % n

    print('#{} {}'.format(idx, oven[oven_idx]+1))
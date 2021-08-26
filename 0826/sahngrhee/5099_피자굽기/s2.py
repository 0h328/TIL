import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split())) # 피자 치즈의 양
    # Ci = list(enumerate(Ci))
    oven = [0] * N

    result = True
    idx = 0
    cnt = 0

    while cnt < N:                       # 첫 oven을 구성
        oven[cnt] = Ci[idx]
        idx += 1
        cnt += 1

    while idx < M:                        # oven을 돌린다 !
        if cnt >= N:
            cnt = 0
        if oven:                          # oven이 True이면
            while result:                 # True면 계속 반복
                pizza = oven.pop(0)
                pizza = pizza // 2
                if pizza <= 0:            # pizza가 0과 같거나 작으면
                    pizza = 0
                    result = False
                oven.append(pizza)        # pizza를 oven에 넣어줌
        if idx < M:                       # 만약 idx가 오븐 크기(M)보다 작으면
            oven[-1] = Ci[idx]            # 다시 넣어줌
            result = True
            idx += 1
        else:
            result = False


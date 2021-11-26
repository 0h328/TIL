import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N: 화덕의 크기 / M: 피자의 개수
    pizza = list(map(int, input().split())) # 피자
    oven = []                               # 화덕

    for i in range(N):
        oven.append((i+1, pizza[i]))        # i+1 (피자 번호), pizza[i]
    next_pizza = N                          # 피자를 N번부터 넣어야 함
    # last_pizza = -1

    while len(oven) > 1:                    # 화덕에 피자가 1개 남기 전까지
        num, cheese = oven.pop(0)           # 피자 번호 / 치즈
        cheese //= 2                        # 치즈를 줄이고
        last_pizza = num                    # 현재 꺼낸 피자는 마지막 피자로 이동
        if cheese:                          # 이때 치즈가 남아있다면
            oven.append((num, cheese))      # 해당 피자는 다시 화덕으로
        else:                               # 치즈가 남아있지 않은 경우는 위의 pop을 통해 이미 꺼내진 상태
            if next_pizza < M:              # 아직 넣어야 할 피자가 남아있다면
                oven.append((next_pizza+1, pizza[next_pizza]))  # 다음 피자를 넣고
                next_pizza += 1                                 # 다음 피자를 위한 인덱스 증가

    ans = oven[0][0]
    print('#{} {}'.format(tc, ans))
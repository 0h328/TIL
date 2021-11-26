import sys

sys.stdin = open('input.txt')

for test in range(1, 1 + int(input())):
    N, M = list(map(int, input().split()))

    data = list(map(int, input().split()))

    total_pizza = [(i + 1, data[i]) for i in range(M)]# 전체 피자에 인덱스 붙여주기

    oven = total_pizza[:N]                              # 오븐 안에 들어가있는 피자
    outside = total_pizza[N:]                           # 밖에 있는 피자

    while len(oven) != 1:                           # 오븐안에 있는 피자가 1이되면 브레잌
        index, cheese = oven.pop(0)                 # 튜플형태기 때문에 값변환을 위해서 따로 변수 설정
        cheese //= 2                                # 치즈만 나눠준다

        if cheese:                                  # 나눴을때 치즈가 이미 있다면
            oven.append((index, cheese))            # 더해주고
        else:                                        # 없다면
            if outside:                              # 그리고 밖에 남은 피자가 있다면
                oven.append(outside.pop(0))             # 그걸 더해준다.

    print('#{} {}'.format(test, oven.pop()[0]))
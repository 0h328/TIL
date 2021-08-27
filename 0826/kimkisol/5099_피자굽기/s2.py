import sys

sys.stdin = open('input.txt')


def Count_Zeros(oven):
    cnt = 0
    for pizza in oven:
        if pizza[1] == 0:
            cnt += 1
    return cnt


# 1. sol : 현정 (아직 enumerate 사용 못해서 index로 답이 나오지 않아요ㅠㅠ 참고해주세용..)
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # Ci = list(map(int, input().split())) # 피자 치즈의 양
    Ci = []
    for num, pizza in enumerate(list(map(int, input().split())), 1):  # 피자 치즈 양
        Ci.append([num, pizza])

    oven = [0] * N

    result = True
    idx = 0
    cnt = 0

    while cnt < N:  # 첫 oven을 구성
        oven[cnt] = Ci[idx]
        idx += 1
        cnt += 1

    # while Count_Zeros(oven) < len(oven) - 1:
    while list(map(lambda x: x[1], oven)).count(0) < len(oven) - 1:
        while True:
            pizza = oven.pop(0)
            pizza[1] = pizza[1] // 2
            oven.append(pizza)
            if pizza[1] == 0:
                break

        if idx < M:
            oven[N - 1] = Ci[idx]
            idx += 1

    for pizza in oven:
        if pizza[1]:
            last_pizza = pizza[0]

    print('#{} {}'.format(tc, last_pizza))

# print(list(map(lambda x : x[1], [(1, 0), (2, 0), (3, 1)])).count(0))

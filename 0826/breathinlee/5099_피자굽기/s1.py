import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())                # N : 화덕의 크기, M : 피자 개수
    cheese = list(map(int, input().split()))        # M개의 피자에 뿌려진 치즈의 양
    pizza = []

    # 한바퀴 돌고 다시 제자리로 왔을 때, 치즈의 양은 c//2
    # 치즈의 양이 0이 되면 꺼내

    for i in range(M):
        pizza.append([i+1, cheese[i]])
    in_oven = pizza[:N]
    out_oven = pizza[N:]
    # print(in_oven)
    while len(in_oven) > 1:
        rotate_oven = in_oven.pop(0)
        # print(rotate_oven)
        rotate_oven[1] //= 2
        if rotate_oven[1] > 0:                       # 치즈가 다 녹지 않았으면
            in_oven.append(rotate_oven)
        else:                                        # 치즈가 녹았으면
            if len(out_oven) != 0:                   # out_oven에 피자가 있다면
                in_oven.append(out_oven.pop(0))      # out_oven에 있는 피자 in_oven에 추가

    print('#{} {}'.format(tc, in_oven[0][0]))


import sys
sys.stdin = open('input.txt')

for _ in range(10):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # print(ladder)

    place = 0  # 지나갔는지 파악하는 발자국 가로 반복될 수 있음
    for i in range(100):
        if ladder[99][i] == 2:
            x = i
            break
    y = 99
    while True: # 얼마나 반복해야하는지 모르니 True
        if (place == 0 or place == 2) and x < 99 and ladder[y][x+1] == 1:  # 순서 중요;;;;;
            x += 1
            place = 2

        elif (place == 0 or place == 1) and x > 0 and ladder[y][x-1] == 1:
            x -= 1
            place = 1

        else:
        # elif (place == 1 or place == 2) and 0 < x < 99:
            y -= 1
            place = 0
            if y == 0:
                break
    print('#{} {}'.format(t, x))

import sys

sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())

    data = [list(map(int, input().split())) for i in range(100)]

    for i in range(100):
        if data[99][i] == 2:
            c = i                           # 목적지 부터 출발
            break
    r = 99

    while r != 0:

        if c > 0 and data[r][c - 1]:         # 왼쪽이동이 가능하다면
            while c > 0 and data[r][c - 1]:  # 계속해서
                c -= 1                       # 왼쪽으로 이동
                                  # 아니라면 위로 이동


        elif c < 99 and data[r][c + 1]:      # 오른쪽 반복
            while c < 99 and data[r][c + 1]:
                c += 1



                                         # 모두 아니라면 위로 이동
        r -= 1

    print('#{} {}'.format(_ + 1, c))

import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    data = [[idx, val, 1] for idx, val in enumerate(temp, start=1)]
    data = deque(data)

    fire_pit = deque()
    in_fire_cnt = 0

    while M > 1:
        if in_fire_cnt < N and data:    # 화덕에 빈 공간 있을 때 피자를 추가해야 하는 경우
            fire_pit.append(data.popleft())
            in_fire_cnt += 1
        else:                           # 화덕에 피자가 다 차있는 경우나 더이상 가져올 피자 없는 경우
            check_idx, check_cheese, rotate_cnt = fire_pit.popleft()
            temp = check_cheese // (2 ** rotate_cnt)
            if temp:
                rotate_cnt += 1
                fire_pit.append([check_idx, check_cheese, rotate_cnt])
            else:
                M -= 1
                in_fire_cnt -= 1

    print('#{} {}'.format(tc, fire_pit[0][0]))


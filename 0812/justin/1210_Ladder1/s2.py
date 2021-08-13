def solve(data):
    next = 'U'                  # 기본이 up
    y = 99
    for x in range(len(data)):  # 리스트의 크기 만큼 반복을 돌며
        last_row = data[99]     # 마지막 행을 먼저 잡자
        if last_row[x] == 2:    # 만약 last_row의 x행이 2일 때 시작
            while y > 0:        # y는 최고점에 올라갈 때 0 (99부터 시작하도록 가장 위에서 초기화)
                if next == 'U': # (첫 시작은 무조건 올라감) 올라갈 때는, 양 옆을 보며 (이때 우회전과 좌회전이 동시에 가능한 상황은 없음)
                    if x < 99 and data[y][x+1]:  # 우회전 가능 (index 에러 때문에 x < 99 필요)
                        next = 'R'               # 다음은 R
                        x += 1
                    elif x > 0 and data[y][x-1]: # 좌회전 가능
                        next = 'L'               # 다음은 L
                        x -= 1
                    else:                        # 우/좌회전이 안된다면 올라가자
                        y -= 1
                else:                            # 양쪽(R, L) 을 갈 때는 위를 보며
                    if data[y - 1][x]:           # 양 끝은 무조건 위로 가자
                        next = 'U'
                        y -= 1
                    elif next == 'R':            # 우회전 가능이면 오른쪽으로 이동
                        x += 1
                    elif next == 'L':            # 좌회전 가능이면 왼쪽으로 이동
                        x -= 1
            return x                             # y가 0이 되면 종료되고 그때의 x 값 반환

import sys
sys.stdin = open('input.txt')
for _ in range(1, 11):
    tc = input()
    data = [list(map(int, input().split())) for _ in range(100)]
    ans = solve(data)
    print('#{} {}'.format(tc, ans))
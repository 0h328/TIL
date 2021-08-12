'''
* 참고
도착해야할 지점은 마지막 행 요소들 중 값이 2이다.

1. 밑에서부터 거꾸로 올라감
2. 위로 올라가면서 왼쪽 오른쪽에 0이 아닌 값이 있는지 확인
3. 값이 있다면 왼쪽 오른쪽으로 진행
4. 왼쪽 오른쪽으로 계속 진행하다가 0 또는 경계선 발견시 위로 이동
5. 반복

* 예상 시간복잡도 - O(N^2)
for - O(N)
    while - O(N)
'''

import sys
sys.stdin = open('input.txt')


for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    x = ladder[99].index(2)                             # 초기 x좌표 설정

    for r in range(99, -1, -1):                         # 도착지부터 출발하여 위로 올라감
        sign = False                                    # 옆으로 이동했는지 여부, True:이동, False:이동 안함

        while 0 <= x-1 and ladder[r][x-1] == 1:         # 인덱스 범위 내이면서 왼쪽의 값이 1이라면 반복
            x -= 1
            sign = True                                 # 왼쪽으로 이동했으므로 변수에 True 저장

        if not sign:                                    # 왼쪽으로 이동하지 않은 경우
            while x+1 < 100 and ladder[r][x+1] == 1:    # 인덱스가 범위 내, 오른쪽 값이 1이라면 반복
                x += 1

    print('#{} {}'.format(tc, x))
'''
위에서 출발 가능한 출발지에서 모두 출발하는 경우

* 예상 시간복잡도 - O(N^3)
while - O(N)
    for - O(N)
        while - O(N)
'''


import sys
sys.stdin = open('input.txt')


for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    idx = 0
    while idx < 100:
        if ladder[0][idx] == 1:                                 # 출발선일때
            x = idx                                             # x 좌표 설정

            for r in range(100):                                # 높이가 밑으로 출발
                sign = False                                    # 좌우 이동 여부 판단 변수

                while 0 <= x-1 and ladder[r][x-1] == 1:         # 왼쪽이 인덱스 범위이면서 값이 1이
                    x -= 1
                    sign = True                                 # 왼쪽으로 이동했으므로 sign True

                if not sign:                                    # 왼쪽으로 이동하지 않았으면
                    while x+1 < 100 and ladder[r][x+1] == 1:    # 오른쪽이 인덱스 범위이면서 값이 1이면
                        x += 1

            if ladder[99][x] == 2:                              # 도착한곳이 출구일때 종료
                break

            idx += 2                                            # 출발한곳 바로 다음 출발지는 최소 한칸 이상이 띄워지므로 +2
            continue

        idx += 1                                                # 출발지가 아니면 바로 다음 인덱스 검색

    print('#{} {}'.format(tc, idx))
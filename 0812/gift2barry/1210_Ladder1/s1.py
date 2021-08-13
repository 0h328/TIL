import sys
sys.stdin = open('input.txt')

# 문제점:
# 4번째 tc 는 오답, 5번째 tc는 IndexError
# 예상 원인:
# 좌 우측 벽에 닿을때 if 문에 인덱스에러

for tc in range(1, 11):

    tc_number = int(input())
    # 사다리 불러오기
    ladder = [list(map(int, input().split())) for _ in range(100)]

    col_idx = ladder[99].index(2)       #값이 2인 목표지점 찾기

    y = col_idx                         # y좌표 만들기

    x = 99                              # x 좌표 만들기

    right = left = 1                    # 좌 우측 값 1 할당

    while x > 0:                        # 정답지점 찾기

        if ladder[x][y-1] == left or ladder[x][y+1] == right:   # 좌 or 우 에 길이 있으면
            while ladder[x][y-1] == left:   # 좌측이 1 일때 계속 좌측이동
                y -= 1
                if ladder[x-1][y] == 1:     # 위에 길이 생기면 한칸 up
                    x -= 1
            while ladder[x][y+1] == right:  # 우측이 1 일때 계속 우측이동
                y += 1
                if ladder[x-1][y] == 1:   # 위에 길이 생기면 한칸 up
                    x -= 1
        else:                               # 좌 or 우 에 길 없으면 한칸 up
            x -= 1

    ans = y
    print('#{} {}'.format(tc, ans))




# 패작1

# thought process:
# 숫자2에서 출발
# 올라가면서 계속 좌 우를 확인
# 좌 측에 숫자1 = 좌측숫자1없어질때까지 좌측 이동
# 우 측에 숫자1 = 우측숫자1없어질때까지 우측 이동
# 없어지면 다시 위로 향한다
# 위로향하는게 100번 지나면
# 현재위치의 행 값 반환

#     좌  우
# dy = [-1, 1]
#
# def ans_finder():
#     T = int(input())        # 10개의 케이스
#     ladder = [list(map(int, input().split())) for _ in range(100)]
#     col_idx = ladder[99].index(2)
#
#     for tc in range(T):
#
#         for i in range(100):        # 사다리 꼭대기까지 가기위해 100 반복
#             ladder[99 - i][col_idx] # 먼저 한칸 올라가고
#
#             if ladder[99 - i][col_idx - 1] == 1:    # 좌측에 길이 있으면
#
#                 while
#
#             elif ladder[99 - i][col_idx + 1] == 1:  # 우측에 길이 있으면
#
#
#
#
#
#     def go_left():
#
#     def go_right():
#         pass
#
# ans_finder()

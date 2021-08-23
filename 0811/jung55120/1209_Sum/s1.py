import sys
sys.stdin = open('input.txt')

for _ in range(10) :
    tc = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]  # arr에 100개의 input을 받기

    max_num = 0

    for n in range(100):        # 행의 합
        sum = 0                 # 행이 100개라서 100번 리셋해줘야 함
        for m in range(100):    # rc
            sum += arr[n][m]
            if sum > max_num:   # 만약 sum이 max_num 보다 크면
                max_num = sum   # sum 값을 max_num에 저장

    for n in range(100):        # 열의 합
        sum = 0
        for m in range(100):
            sum += arr[m][n]
            if sum > max_num:
                max_num = sum

    sum = 0                     # 대각선은 합계가 1번만
    for n in range(100):        # 대각선 1의 합
        sum += arr[n][n]
    if sum > max_num :          # 행,열과 다르게 1번만 sum 값을 체크해주면 됨
        max_num = sum

    sum = 0
    for n in range(99,-1,-1) :  # 대각선 2의 합
        sum += arr[n][99-n]
    if sum > max_num :
        max_num = sum

    print('#{0} {1}'.format(tc, max_num))
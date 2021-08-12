import sys
sys.stdin = open('input.txt')

for _ in range(10) :
    tc = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]  # arr에 100개의 input을 받기

    max_num = 0

    for n in range(100):
        sum = 0
        for m in range(100) :
            sum += arr[n][m]
            if sum > max_num :
                max_num = sum

    for n in range(100):
        sum = 0
        for m in range(100) :
            sum += arr[m][n]
            if sum > max_num :
                max_num = sum

    for n in range(100):
        sum = 0
        for m in range(100) :
            if n == m :
                sum += arr[n][m]
                if sum > max_num :
                    max_num = sum

    for n in range(99,-1,-1) :
        sum = 0
        for m in range(99,-1,-1) :
            if n == m :
                sum += arr[m][n]
                if sum > max_num :
                    max_num = sum

    print('#{0} {1}'.format(tc, max_num))




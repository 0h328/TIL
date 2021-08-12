import sys
sys.stdin = open('input.txt')

N = int(input())


for tc in range(1, N+1):
    numbers = list(map(int, input().split()))
    A_l = 1
    B_l = 1

    A_r = numbers[0]
    B_r = numbers[0]

    A_t = numbers[1]
    B_t = numbers[2]

    A_cnt = 0
    B_cnt = 0
    A_c = (A_l + A_r)//2
    B_c = (B_l + B_r)//2
    while True:
        A_cnt += 1
        if A_c > A_t:
            A_l = (A_l + A_r)//2
        elif A_c < A_t:
            A_r = (A_l + A_r)//2
        else:
            break

    while True:
        B_cnt += 1
        if B_c//2 > B_t:
            B_l = (B_l + B_r)//2
        elif (B_l + B_r)//2 < B_t:
            B_r = (B_l + B_r)//2
        else:
            break


    if A_cnt > B_cnt:
        print('#{} A'.format(tc))
    elif A_cnt < B_cnt:
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))

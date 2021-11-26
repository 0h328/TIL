import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    cnt_list = [0] * 10
    my_list = list(map(int, input()))
    # print(my_list)
    for i in my_list:
        cnt_list[i] += 1
    cnt = 0
    result = 0
    # print(cnt_list)
    while cnt < 10:
        if cnt_list[cnt] >= 3:
            cnt_list[cnt] -= 3
            result += 1
            continue

        if cnt_list[cnt] >= 1 and cnt_list[cnt+1] >= 1 and cnt_list[cnt+2] >= 1:
            cnt_list[cnt] -= 1
            cnt_list[cnt+1] -= 1
            cnt_list[cnt+2] -= 1
            result += 1
            continue

        cnt += 1

    if result == 2:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    my_list = list(map(int, input()))
    new_list = [0] * 10
    check = 0
    # print(my_list)
    # print(new_list)
    for i in range(len(my_list)):
        new_list[my_list[i]] += 1
    # print(new_list)

    cnt = 0


    while cnt < 10:
        if new_list[cnt] >= 3:
            new_list[cnt] -= 3
            check += 1
            continue

        if new_list[cnt] >= 1 and new_list[cnt + 1] >= 1 and new_list[cnt + 2] >= 1:
            new_list[cnt] -= 1
            new_list[cnt + 1] -= 1
            new_list[cnt + 2] -= 1
            check += 1
            continue
        cnt += 1

    if check == 2:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))

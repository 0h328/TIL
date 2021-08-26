import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    my_list = list(map(int, input().split()))

    result = True
    cnt = 1

    while result:
        number = my_list.pop(0)
        number -= cnt
        if cnt == 6:
            cnt = 1
        if number <= 0:
            number = 0
            result = False
        cnt += 1
        my_list.append(number)

        # print('#{}'.format(tc + 1), end=' ')
    print('#{}'.format(tc), end=' ')
    print(*my_list)

    # while True:
    #     my_list.append(my_list[idx] - cnt)
    #     my_list[idx] = 0
    #     idx += 1
    #     cnt += 1
    #     if my_list[idx] == 0:
    #         break
    # print(my_list)

    # 망했군

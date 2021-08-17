import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    my_str1 = input()
    my_str2 = input()
    my_list = []

    for i in my_str1:
        my_list.append(my_str2.count(i))

    print('#{} {}'.format(tc, max(my_list)))


    my_result = 0
    for j in my_str1:
        cnt = 0
        for k in my_str2:
            if j == k:
                cnt +=1

        if my_result < cnt:
            my_result = cnt

    print('#{} {}'.format(tc, my_result))

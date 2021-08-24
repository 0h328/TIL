import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    my_list = list(map(int, input().split()))
    cnt_list = [0] * 10
    sort_list = [0] * len(my_list)

    for i in my_list:
        cnt_list[i] += 1

    for i in range(1, len(cnt_list)):
        cnt_list[i] += cnt_list[i-1]

    # print(cnt_list)
    for i in range(len(sort_list)):
        sort_list[cnt_list[my_list[i]]-1] = my_list[i]
        # cnt_list[my_list[i]] -= 1 # 왜??

    print(sort_list)


    # print(cnt_list)


    # print(tc)
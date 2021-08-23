import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    my_list = list(map(int, input().split()))
    cnt_list = [0]*10
    sort_list = [0] * len(my_list)

    for i in my_list:
        cnt_list[i] += 1

    print(cnt_list)
    cnt = 0
    for i in range(len(cnt_list)):
        while cnt_list[i] > 0:
            sort_list[cnt] = i
            cnt_list[i] -= 1
            cnt += 1



    print(sort_list)
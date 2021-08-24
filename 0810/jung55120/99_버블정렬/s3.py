import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    my_list = list(map(int, input().split()))

    for j in range(1, len(my_list)):
        for i in range(1, len(my_list)-j+1):
            if my_list[i] < my_list[i-1]:
                my_list[i], my_list[i - 1] = my_list[i-1], my_list[i]

    print(my_list)
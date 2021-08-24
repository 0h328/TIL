import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    my_list = list(map(int, input().split()))
    # print(my_list)
    for j in range(len(my_list)):
        for i in range(1, len(my_list)-j):
            if my_list[i-1] > my_list[i]:
                my_list[i-1], my_list[i] = my_list[i], my_list[i-1]

    print(my_list)
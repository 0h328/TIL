import sys
sys.stdin = open('input2.txt')


# for i in my_list:
#     if i == 2:
#         print(1)

def find_num(my_list, num):
    for i in range(len(my_list)):
        if my_list[i] > num:
            return 0

        elif my_list[i] == num:
            return 1


my_list = list(map(int, input().split()))
print(my_list)
print(find_num(my_list, 5))
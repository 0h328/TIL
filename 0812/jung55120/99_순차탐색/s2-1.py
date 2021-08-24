import sys
sys.stdin = open('input2.txt')

def find_num(my_list, num):
    for i in range(len(my_list)):
        if my_list[i] == num:
            return 1

    return 0

my_list = list(map(int, input().split()))
print(find_num(my_list, 5))
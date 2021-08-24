def solve(my_str1, my_str2):
    # if len(my_str1) != len(my_str2):
    #     return False
    # else:
    #     for i in my_str1:
    #         for j in my_str2:
    #             if i == j:
    #                 return True
    #             else:
    #                 return False
    idx = 0
    while idx < len(my_str1) and idx < len(my_str2):
        idx += 1
        if my_str1[idx] != my_str2[idx]:
            return False
        else:
            return True

import sys
sys.stdin = open('input.txt')
my_str1 = input()
my_str2 = input()

print(solve(my_str1, my_str2)) # False
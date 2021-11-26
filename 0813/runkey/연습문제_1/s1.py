def solve(my_str1, my_str2):
    if len(my_str1) >= len(my_str2):
        min_len = len(my_str2)
    else:
        min_len = len(my_str1)
    for i in range(min_len):
        try:
            if my_str1[i] != my_str2[i]:
                return False
        except IndexError:
            return False
    return True

import sys
sys.stdin = open('input.txt')
my_str1 = input()
my_str2 = input()

print(solve(my_str1, my_str2)) # False
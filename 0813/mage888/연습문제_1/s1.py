def solve(my_str1, my_str2):
    idx = 0
    if len(my_str1) != len(my_str2):
        return False
    else:
        while idx < len(my_str1) and idx < len(my_str2):
            if my_str1[idx] != my_str2[idx]:
                return False
            idx += 1
    return True

import sys
sys.stdin = open('input.txt')
my_str1 = input()
my_str2 = input()

print(solve(my_str1, my_str2)) # False

def solve(my_str1, my_str2):

    if my_str1 == my_str2:
        return True

    return False

import sys
sys.stdin = open('input.txt')
my_str1 = input()
my_str2 = input()

print(solve(my_str1, my_str2)) # False
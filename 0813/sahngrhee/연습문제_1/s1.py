def solve(my_str1, my_str2):
    a = len(my_str1)
    b = len(my_str2)
    if a > b:
        for i in range(a):
            if my_str1[i] != my_str2[i]:
                return False
    else:
        for i in range(b):
            if my_str1[i] != my_str2[i]:
                return False
    return True

import sys
sys.stdin = open('input.txt')
my_str1 = input()
my_str2 = input()

print(solve(my_str1, my_str2))
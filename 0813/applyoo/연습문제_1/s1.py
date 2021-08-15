def solve(my_str1, my_str2):
    return my_str1 == my_str2

import sys
sys.stdin = open('input.txt')

my_str1 = input()
my_str2 = input()

print(solve(my_str1, my_str2))
def solve(my_str1, my_str2):
    if my_str1 == my_str2:
        return True
    return False

# my_str1과 my_str2가 같은지 여부 확인 -> T/F

import sys
sys.stdin = open('input.txt')
my_str1 = input()
my_str2 = input()

print(solve(my_str1, my_str2)) # False
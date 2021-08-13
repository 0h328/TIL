def solve(my_str1, my_str2):
    i = 0
    j = 0
    while i < len(my_str1) and j < len(my_str2):
        if my_str1[i] == my_str2[j]:
            i += 1
            j += 1
        else:
            return False
    return True


import sys
sys.stdin = open('input.txt')
my_str1 = input()
my_str2 = input()

print(solve(my_str1, my_str2)) # False


def solve(my_str1, my_str2):
    i = 0
    j = 0
    if len(my_str1) == len(my_str2):
        while j < len(my_str2) and i < len(my_str1):
            if my_str1[i] != my_str2[j]:
                i = i - j
                j = -1
            i += 1
            j += 1
        if j == len(my_str2):
            return True
        else:
            return False
    else:
        return False


import sys
sys.stdin = open('input.txt')
my_str1 = input()
my_str2 = input()

print(solve(my_str1, my_str2)) # False
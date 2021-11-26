import sys
sys.stdin = open('input.txt')

def solve(my_str1, my_str2):
    if len(my_str1) != len(my_str2):
        return False
    else:
        for i in range(len(my_str1)-1):
            if my_str1[i] != my_str2[i]:
                return False
        return True

my_str1 = input()
my_str2 = input()

print(solve(my_str1, my_str2)) # False
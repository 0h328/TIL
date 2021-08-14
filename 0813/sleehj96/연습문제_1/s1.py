import sys


def solve(my_str1, my_str2):

    str1_length = len(my_str1)
    str2_length = len(my_str2)

    if str1_length != str2_length:
        return False

    else:
        for idx in range(str1_length):
            if my_str1[idx] != my_str2[idx]:
                return False
        else:
            return True


sys.stdin = open('input.txt')

my_str1 = input()
my_str2 = input()

print(solve(my_str1, my_str2)) # False
import sys
sys.stdin = open('input.txt')

T = int(input())

# for tc in range(1, T + 1):
#     my_str1 = input()
#     my_str2 = input()
#     my_result = 0
#
#     if my_str2.count(my_str1) > 0:
#         my_result = 1
#     else:
#         my_result = 0
#
#     print('#{} {}'.format(tc, my_result))

def find_letters(letters, pattern):
    for i in range(0, len(letters) - len(pattern) + 1):
        tmp = 0
        for j in range(len(pattern)):
            if letters[i+j] != pattern[j]:
                break
        else:
            tmp += 1

for tc in range(1, T + 1):
    pattern = input()
    letters = input()

    print('#{} {}'.format(tc, find_letters(letters, pattern)))
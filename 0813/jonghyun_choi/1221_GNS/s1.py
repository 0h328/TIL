import sys
sys.stdin = open('input.txt')

T = int(input())
str_number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for _ in range(T):
    case_number, len_number = input().split()
    number_list = list(input().split())
    i = 0
    j = 0
    move_index = 0
    while i < len(str_number)-1:
        while j < int(len_number):
            if number_list[j] == str_number[i]:
                number_list[move_index] , number_list[j] = number_list[j], number_list[move_index]
                move_index += 1
            j += 1
        j = move_index
        i += 1
    print(case_number)
    print(' '.join(number_list))
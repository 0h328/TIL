import sys

sys.stdin = open('input.txt', encoding='UTF-8')

other_planet_num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
case_num = 1
while case_num <= T:
    input_str = input().split()
    test_case = input_str[0]
    str_length = input_str[1]
    # print(str_length)

    test_str = input().split()
    earth_num_list = []
    for e1 in test_str:
        earth_num_list.append(other_planet_num_list.index(e1))
    earth_num_list.sort()
    # print(earth_num_list)


    print('{}'.format(test_case))
    for e2 in earth_num_list:
        print(other_planet_num_list[e2], end = ' ')
    print()
    # break
    case_num += 1
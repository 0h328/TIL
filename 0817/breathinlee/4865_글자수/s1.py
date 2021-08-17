import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    # str1_dict = {}
    # for i in range(len(str1)):
    #     str1_dict[str1[i]] = str1.count(str1[i])

    str2_dict = {}
    for i in range(len(str1)):
        str2_dict[str1[i]] = str2.count(str1[i])
    max_val = max(str2_dict.values())

    print('#{} {}'.format(tc, max_val))
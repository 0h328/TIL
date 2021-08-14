import sys
sys.stdin = open("input.txt")


T = int(input())
num_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
num_dict2 = {0 : 'ZRO', 1 : 'ONE', 2 : 'TWO', 3 : 'THR', 4 : 'FOR', 5 : 'FIV', 6 : 'SIX', 7 : 'SVN', 8 : 'EGT', 9 : 'NIN'}

for tc in range(1, T+1):
    tc_info = list(input().split())
    data = list(input().split())

    for i in range(len(data)):
        data[i] = num_dict.get(data[i])

    data.sort()

    for i in range(len(data)):
        data[i] = num_dict2.get(data[i])

    print('#{}'. format(tc))
    print(*data)



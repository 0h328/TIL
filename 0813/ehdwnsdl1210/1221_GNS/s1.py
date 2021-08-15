import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N, B = map(str, input().split())
    L = list(map(str, input().split()))

    num = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    reverse_num = {0:'ZRO', 1:'ONE', 2:'TWO', 3:'THR', 4:'FOR', 5:'FIV', 6:'SIX', 7:'SVN', 8:'EGT', 9:'NIN'}

    my_list = []
    for i in L:
        my_list.append(num[i])

    my_list.sort()

    my_result = []
    for j in my_list:
        my_result.append(reverse_num[j])

    print(N)
    print(*my_result)
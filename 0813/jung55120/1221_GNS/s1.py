import sys
sys.stdin = open('input.txt')



language = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

# 첫번째 방법
TC = int(input())
for _ in range(1, TC + 1):
    tc, numbers = map(str, input().split())
    my_lst = list(map(str, input().split()))

    result = []

    for j in range(len(language)):
        for i in range(len(my_lst)):
            if my_lst[i] == language[j]:
                result.append(my_lst[i])
    result = ' '.join(result)
    print('{0}\n{1}'.format(tc, result))

# 두번째 방법

# language = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
# TC = int(input())                              # 왜 얘가 더 오래 걸리지? 궁금
# for _ in range(1, TC+1):
#     tc, numbers = map(str, input().split())
#     my_lst = list(map(str, input().split()))
#
#     result = []
#
#
#     for j in range(len(language)):
#         for i in range(len(my_lst)-1,-1,-1):
#             if my_lst[i] == language[j]:
#                 result.append(my_lst[i])
#                 my_lst.remove(my_lst[i])
#     result = ' '.join(result)
#     print('{0}\n{1}'.format(tc, result))
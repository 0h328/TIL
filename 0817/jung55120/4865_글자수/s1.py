import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    str1 = list(input())
    str2 = list(input())
    dict_str1 = dict()
    for i in range(len(str1)):
        dict_str1[str1[i]] = 0
        for j in range(len(str2)):
            if str2[j] == dict_str1[i]:
                dict_str1[i] += 1

    print(dict_str1)

    print(str2)




















# T = int(input())
# for tc in range(1, T+1):
#     word = input()
#     sentence = input()
#
#     cnt = {}
#     for target in word:
#         cnt[target] = 0
#
#     ans = 0
#
#     for char in sentence:
#         if char in cnt:
#             cnt[char] += 1
#
#     print('#{} {}'.format(tc, max(cnt.values())))
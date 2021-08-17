import sys
sys.stdin = open('input.txt')






















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
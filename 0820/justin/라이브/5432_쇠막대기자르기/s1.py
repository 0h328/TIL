import sys
sys.stdin = open('input.txt')

# T = int(input())
# #1. stack 활용
# for tc in range(1, T+1):
#     iron_bar = input()
#
#     stack = []
#     ans = 0
#
#     for i in range(len(iron_bar)):
#         if iron_bar[i] == '(':
#             stack.append('(')  # 열린 괄호면 넣고
#         else:
#             stack.pop()        # 아니라면 빼자
#             if iron_bar[i-1] == '(':
#                 ans += len(stack)
#             else:
#                 ans += 1
#     print('#{} {}'.format(tc, ans))
    
################################################
#2. stack 없이
T = int(input())
for tc in range(1, T+1):
    iron_bar = input()

    cnt = 0
    ans = 0

    for i in range(len(iron_bar)):
        if iron_bar[i] == '(':
            cnt += 1
        elif iron_bar[i-1] == '(':
            cnt -= 1
            ans += cnt
        else:
            cnt -= 1
            ans += 1
    print('#{} {}'.format(tc, ans))
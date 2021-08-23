import sys
sys.stdin = open('input.txt')

# T = int(input())

# for tc in range(1, T+1):
#     L = input()
#     stack = []
#     ans = 0

'''
    for i in range(len(L)):
        if L[i] == '(':
            stack.append(L[i])
        elif L[i] == ')':
            if L[i-1] == '(':
                stack.pop()
                ans += len(stack)
            elif L[i-1] == ')':
                stack.pop()
                ans += 1
                
    print('#{} {}'.format(tc, cnt))
'''
'''
    for i in range(len(L)):
        if L[i] == '(':
            stack.append('(')
        else:
            stack.pop()
            if L[i-1] == '(':
                ans += len(stack)
            else:
                ans += 1
    print('#{} {}'.format(tc, cnt))
'''

# No Stack
T = int(input())

for tc in range(1, T+1):
    L = input()
    ans = 0
    cnt = 0

    # for i in range(len(L)):
    #     if L[i] == '(':
    #         cnt += 1
    #     else:
    #         cnt -= 1
    #         if L[i - 1] == '(':
    #             ans += cnt
    #         else:
    #             ans += 1
    #
    # print('#{} {}'.format(tc, ans))

    for i in range(len(L)):
        if L[i] == '(':
            cnt += 1
        elif L[i - 1] == '(':
            cnt -= 1
            ans += cnt
        else:
            cnt -=1
            ans += 1

    print('#{} {}'.format(tc, ans))

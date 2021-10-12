import sys
sys.stdin = open('input.txt')
#아니. 이해가 안가네..?!
#닫는 괄호 나왔을 때, 스택에 여는 괄호 없으면 걍 바로 break하고 답 없는거 아닌가??
T = int(input())
#print('{} {}'.format}1, 2)) 이렇게 되면 index error생김. 앞에 짝 맞는거 다 나가서 stack 비어있는데 돌아가기 때문
# for tc in range(1, T+1):
#     sentence = input()
#     stack = []
#     for chr in sentence:
#         if chr == '{' or chr == '(':
#             stack.append(chr)
#         if chr == '}' and stack[-1] == '{':
#             stack.pop()
#         elif chr == ')' and stack[-1] == '(':
#             stack.pop()
#     if len(stack):
#         ans = 0
#     else:
#         ans = 1

for tc in range(1, T+1):
    sentence = input()
    stack = []
    for chr in sentence:
        if chr == '{' or chr == '(':
            stack.append(chr)
        if chr == '}':
            if len(stack) and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(chr)
        elif chr == ')':
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
    if len(stack):
        ans = 0
    else:
        ans = 1


    print('#{} {}'.format(tc, ans))
import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    sentence = input()
    flag = 0
    stack = []
    for i in range(len(sentence)):
        if sentence[i] == '{' or sentence[i] == '(':
            stack.append(sentence[i])
        elif sentence[i] == '}'or sentence[i] == ')':
            if len(stack) == 0:
                flag = 1
            elif stack:
                if (stack[-1] == '{' and sentence[i] == ')') or (stack[-1] == '(' and sentence[i] == '}'):
                    final = 0
                    break
                else:
                    stack.pop()
    if flag == 1 or stack:
        final = 0
    else:
        final = 1
    print('#{} {}'.format(tc + 1, final))
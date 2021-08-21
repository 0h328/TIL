import sys
sys.stdin = open("input.txt")

def right_pair(data):
    stack = []
    for d in data:
        if d == '(' or d == '{':
            stack.append(d)
        elif d == ')' or d == '}':
            if len(stack) == 0:                            # stack에 아무것도 없으면,
                return 0
            elif d == '}' and stack[-1] == '(':
            # elif d == '}' and stack.pop() == '(':
                return 0
            elif d == ")" and stack[-1] == '{':
            # elif d == ')' and stack.pop() == '{':
                return 0
            else:                                         # 주석대로 진행하면, else구문 생략 가능
                stack.pop()


    if stack:                                             # stack에 '(' 또는 '{' 가 남아있다면,
        return 0
    else:
        return 1


T = int(input())
for tc in range(1, T+1):
    data = input()
    print('#{} {}'.format(tc, right_pair(data)))






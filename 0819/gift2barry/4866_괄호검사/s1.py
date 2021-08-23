import sys
sys.stdin = open('input.txt')

def check_match(data):

    for i in data:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and '(' == stack[-1]:    # and 는 조심하쟈..
                stack.pop()
            else:
                return 0
        elif i == '}':
            if len(stack) != 0 and '{' == stack[-1]:
                stack.pop()
            else:
                return 0

    if len(stack) == 0:
        return 1
    else:
        return 0

for tc in range(1, int(input())+1):
    stack = []
    data = list(map(str, input()))

    print('#{} {}'.format(tc, check_match(data)))

# 생각 5분
# 풀이 28분
# 디버깅 10분
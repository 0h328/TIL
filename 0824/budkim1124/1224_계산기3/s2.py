N = 11
data = '3+(4+5)*6+7'
stack = []
result = []

for i in range(N):

    if data[i] == '+':  # +인 경우
        while stack:
            if stack[-1] == '(':
                break
            else:
                result.append(stack.pop())
        stack.append(data[i])

    elif data[i] == '*':  # *인 경우
        while stack and stack[-1] == '*':
            result.append(stack.pop())
        stack.append(data[i])

    elif data[i] == '(':
        stack.append(data[i])

    elif data[i] == ')':
        while stack:
            if stack[-1] == '(':
                stack.pop()
                break
            result.append(stack.pop())

    else:
        result.append(data[i])

while stack:
    result.append(stack.pop())

print(result)
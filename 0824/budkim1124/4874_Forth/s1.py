stack = []
result = []
data = input()
i=0

while data[i] != '.':
    if data[i] in ['+','-','*','/'] and len(stack) >= 2:
        while stack:
            result.append(stack.pop())
    elif data[i].isdigit():
        stack.append(data[i])
    else:
        result.append('error')
        break
    i += 1

if len(stack) == 1:
    r
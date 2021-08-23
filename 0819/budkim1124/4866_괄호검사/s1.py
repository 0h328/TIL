
def pop():
    if len(stack) == 0:
        return
    else:
        return stack.pop()

def is_empty():
    if len(stack) == 0:
        return True
    return False

def check_matching(data):
    for i in range(len(data)):


        if data[i] == '(':
            stack.append(data[i])
        elif data[i] == '{':
            stack.append(data[i])
        elif data[i] == "}":
            if stack[-1] == "(":
                break
            elif stack[-1] == "{":
                stack.pop(-1)


        elif data[i] == ')':
            if is_empty():
                return 0
            pop()


    if not is_empty():
        return 0
    else:
        return 1



import sys
sys.stdin = open('input.txt')
T = int(input())
for num in range(T):
    stack = list()
    data = input()

    print("#{} {}".format(num+1, check_matching(data)))

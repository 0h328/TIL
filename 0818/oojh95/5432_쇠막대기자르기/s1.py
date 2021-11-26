import sys
sys.stdin = open('input.txt')
def push(item):
    stack.append(item)

def pop():
    return stack.pop()

def check_matching(data):           # 이 함수에서 push, pop, is_empty 활용
    top = -1
    result = 0
    i = 0
    while i < len(data):
        if data[i] == '(' and data[i + 1] == ')':
            push('(')
            top += 1
            for j in range(top):
                arr[j] += 1
            pop()
            top -= 1
            i += 2
        elif data[i] == '(':
            push('(')
            top += 1
            i += 1
        else:
            pop()
            top -= 1
            result += arr[top + 1] + 1
            arr[top + 1] = 0
            i += 1
    return result

T = int(input())
for test_case in range(1, T + 1):
    data = input()
    stack = []
    arr = [0] * len(data)
    print('#{} {}'.format(test_case, check_matching(data)))



import sys
sys.stdin = open('input.txt')
def push(item):
    stack.append(item)

def pop():
    if is_empty():
        return None
    else:
        return stack.pop()
def is_empty():
    if len(stack):
        return False
    else:
        return True

def check_matching(data):           # 이 함수에서 push, pop, is_empty 활용
    top = -1
    result = 0
    i = 0
    while i < len(data):
        if data[i] == '(':
            push('(')
            top += 1
        else:
            pop()
            if arr[top] == 0:
                for j in range(top):
                    arr[j] += 1
            else:
                result += arr[top] + 1
                arr[top] = 0
            top -= 1
        i += 1
    return result

T = int(input())
for test_case in range(1, T + 1):
    data = input()
    stack = []
    arr = [0] * len(data)
    print('#{} {}'.format(test_case, check_matching(data)))



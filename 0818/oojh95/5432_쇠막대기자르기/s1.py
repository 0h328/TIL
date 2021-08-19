import sys
sys.stdin = open('input.txt')
def push(item):
    stack.append(item)

def pop():
    return stack.pop()

def is_empty():
    if len(stack) == 0:
        return True
    else:
        return False

def check_matching(data):           # 이 함수에서 push, pop, is_empty 활용
    top = -1
    for i in range(len(data)):
        if data[i] == '(':
            push(i)
            top += 1
            arr[i] = top

        else:
            pop()
            arr[i] = top
            top -= 1
    return arr


T = int(input())
for test_case in range(1, T + 1):
    data = input()
    stack = []
    arr = [0] * len(data)
    print(check_matching(data))



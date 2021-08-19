import sys
sys.stdin = open('input.txt')


def push(item):
    stack.append(item)


def pop():
    if len(stack) == 0:
        return None
    return stack.pop()


def is_empty(arr):
    if len(arr):
        return False
    return True


def check_matching(data):           # 이 함수에서 push, pop, is_empty 활용

    pair = {']': '[', '}': '{', ')': '('}

    for i in data:
        if i in ('[', '{', '('):
            push(i)
        else:
            if pair.get(i) != pop():
                return False

    if is_empty(stack):
        return True
    while pop() != None:
        pass
    return False


sys.stdin = open('input.txt')
stack = list()  # []
data = input()
data2 = input()

print(check_matching(data))  # True
print(check_matching(data2)) # False
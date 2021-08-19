def push(item):
    stack.append(item)


def pop():
    stack.pop()


def is_empty():
    if stack:
        return False
    return True


def check_matching(data):  # 이 함수에서 push, pop, is_empty 활용
    open = ["(", "{", "["]

    for bracket in data:
        if bracket in open:  # 여는 괄호 확인
            push(bracket)
        else:  # 닫는 괄호 확인
            if is_empty():  # 앞에 여는 괄호가 부족할 경우
                return False
            pop()

    if is_empty():  # 여는 괄호 남을 경우
        return False
    return True


import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")
stack = list()
data = input()
data2 = input()

print(check_matching(data))  # True
print(check_matching(data2))  # False

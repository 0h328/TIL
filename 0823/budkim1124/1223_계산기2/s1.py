import sys
sys.stdin = open('input.txt')

N = input()
data = input()
stack = []
result = []
#1. 중위 표현식 -> 후위 표현식
for char in data:
    if char == '*':
        stack.append(char)
    elif char == '+':
        # 이경우 고려해야 할 사항?
        # stack이 비어있는지 여부 판단 & stack의 가장 위가 *연산자 인지 확인
        if not stack:
            stack.append(char)
        else:
            if stack[-1] == '*':
                while stack:
                    result.append(stack.pop())
            else:
                stack.append(char)



    else:
        result.append(char)

#2. 후위 표현식 -> 계산

# data
#
# for char in data:
#     if char == '*':
#
#     elif char == '+':
#
#     else:
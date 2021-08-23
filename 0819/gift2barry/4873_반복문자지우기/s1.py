import sys
sys.stdin = open('input.txt')

# thought process: 5분
# 동일한 문자열이 마지막 스택에 있는지 확인하고,
# 있으면 해당 문자열 pop
# 없으면 일단 push
# 반복
# 풀이 16분
for tc in range(1, int(input())+1):

    stack = []
    data = list(map(str, input()))

    for i in range(len(data)):
        if i == 0:                                      # 처음은 무조건 스택에 in
            stack.append(data[i])
        elif len(stack) == 0 or data[i] != stack[-1]:   # 스택 길이가 0이면 무조건 in, 스택안에 문자가 다르면 in
            stack.append(data[i])
        elif data[i] == stack[-1]:                      # 스택안에 문자와 현재 문자가 동일하면 마지막 스택 문자 out
            stack.pop()

    print(len(stack))


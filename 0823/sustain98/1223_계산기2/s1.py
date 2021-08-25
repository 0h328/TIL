import sys
sys.stdin = open('input.txt')

priority = {'*': 1, '+': 0}
stack = []
for idx in range(1, 11):
    length = int(input())
    s = input()
    new_s = ''
    top = -1
    for i in s:
        if i in '+*':
            while stack and priority[stack[top]] >= priority[i]:  #스택에 있는 연산자가 우선순위가 크거나 같은동안 pop해줌
                new_s += stack.pop()
                top -= 1
            stack.append(i)
            top += 1
        else:
            new_s += i
    while stack:                                                    #스택에 아직 연산자가 남아있을수 있음
        new_s += stack.pop()
    print(new_s)

    # 후위표현식 -> 계산
    for i in new_s:
        if i not in '+*':                                           #연산자가 아니면 stack에 넣어줌
            stack.append(i)
        else:                                                       #연산자라면 stack의 값들을 pop해서 계산후 다시 넣어줌
            a = stack.pop()
            b = stack.pop()
            if i == '*':
                stack.append(int(b)*int(a))
            else:  # i == '+'
                stack.append(int(b)+int(a))
    print('#{} {}'.format(idx, stack.pop()))
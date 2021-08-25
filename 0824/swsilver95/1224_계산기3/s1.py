import sys
sys.stdin = open('input.txt')


def infix_to_postfix(my_str):
    isp = {             # 딕셔너리로 isp를 만들어보자!
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        '(': 0,
    }
    postfix = ''        # 최종 후위 표기식을 적어둘 빈 스트링
    stack = []          # 또 스택
    global n            # 입력받은 중위 표기식의 길이를 글로벌 변수로 사용할게요
    for i in range(n):                  # 0. 인덱스 순회 방법 채택 -> 한글자 한글자씩 봅시다.
        if my_str[i].isdigit():         # 1. 글자를 떼어봤더니 숫자면?
            postfix += my_str[i]        # 1-1. 고민 없이 후위 표기식에 바로 추가
        else:                                       # 2. 숫자가 아니다??
            if my_str[i] == '(':                    # 2-1. 여는 괄호가 등장하면
                stack.append(my_str[i])             # 2-2. 일단 push 해놓고 생각
            elif my_str[i] == ')':                  # 3. 닫는 괄호가 등장하면
                while stack[-1] != '(':             # 3-1. 스택이 비거나, 여는 괄호가 등장할 때까지
                    postfix += stack.pop()          # 3-2. pop하는걸 모두 후위 표기식에 추가
                stack.pop()                         # 3-3. 여는 괄호는 필요가 없으므로 pop해서 제거
            else:                                                           # 4. 연산자가 등장하면?
                while stack and isp.get(stack[-1]) >= isp.get(my_str[i]):   # 4-1. 스택이 비거나, 스택 마지막 연산자의 우선순위가 작아질 때까지
                    postfix += stack.pop()                                  # 4-2. pop하는걸 모두 후위 표기식에 추가
                stack.append(my_str[i])                                     # 4-3. 그 다음에 지금 보고 있는 연산자를 push

    while stack:                    # 5. 마지막으로 스택에 남아 있는 연산자들을
        postfix += stack.pop()      # 5-1. 후위 표기식에 뜯어서 추가

    return postfix


def calculate_postfix(ans):
    stack = []
    for i in range(len(ans)):
        if ans[i].isdigit():
            stack.append(ans[i])
        else:
            tmp1 = stack.pop()
            tmp2 = stack.pop()
            if ans[i] == '*':
                stack.append(int(tmp2) * int(tmp1))
            elif ans[i] == '+':
                stack.append(int(tmp2) + int(tmp1))
            elif ans[i] == '-':
                stack.append(int(tmp2) - int(tmp1))
            elif ans[i] == '/':
                stack.append(int(tmp2) / int(tmp1))
    return stack.pop()


for tc in range(1, 11):
    n = int(input())
    text = input()
    postfix = infix_to_postfix(text)
    # print(postfix, '--postfix')
    print('#{} {}'.format(tc, calculate_postfix(postfix)))

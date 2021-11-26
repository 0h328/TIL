import sys
sys.stdin = open('input.txt')

# 딕셔너리로 점수 / top 이용 / ''로 바로 추가해서 답 내도 되고(stack 안써도?)

def calculate_postifx(m):
    stack = []
    for char in m:
        if char == '*':
            b_num = stack.pop()     # 처음 뽑은게 뒷자리
            f_num = stack.pop()     # 담에 뽑은게 앞자리
            stack.append(int(f_num ) * int(b_num))  # 글자니까 int해줘야

        elif char == '+':
            b_num = stack.pop()
            f_num = stack.pop()
            stack.append(int(f_num) + int(b_num))

        else:
            stack.append(char)      # 숫자는 무조건 넣음

    if len(stack) == 1:     # 마지막 1개가 답이라서
        return stack[0]

def change_postfix(n):
    stack = []
    result_list = []    # 후위표기법변환 결과 담을려고

    for char in n:
        if char == '(':
            # while stack and stack[-1] == '(':
            #     stack.pop()       # '('넣었는데 '('가 있으면 빼고 / '('가
            # stack.append(char)
            stack.append(char)      # 제일 강한 친구는 건드려도? (계산기2와 같은 원리?)

        elif char == '*':
            while stack and stack[-1] == '*':
                result_list.append(stack.pop())
            stack.append(char)

        elif char == '+':
            if len(stack) == 0:
                stack.append(char)

            elif stack[-1] == '*':
                while stack and stack[-1] != '(':
                    result_list.append(stack.pop())
                stack.append(char)

            elif stack[-1] == '+':
                while stack and stack[-1] != '(':
                    result_list.append(stack.pop())
                stack.append(char)

            else:
                stack.append(char)

        elif char == ')':
            while stack[-1] != '(':
                result_list.append(stack.pop())
            stack.pop()

        else:
            result_list.append(char)

        # elif char not in ['(', ')', '+', '*']:  # 여기 좀 이상한데? 왜 else는 안되?안돼?
        #     result_list.append(char)

    while len(stack) != 0:
        result_list.append(stack.pop()) # 연산자가 남아있으면 안되니까 마무리로 다 빼주기

    return result_list

for tc in range(1, 11): # TC 10개
    N = int(input())
    notation = input()  # input 고대로

    # print('#{} {}'.format(tc, change_postfix(notation)))
    print('#{} {}'.format(tc, calculate_postifx(''.join(change_postfix(notation)))))
    # 리스트에 담은걸 처음 input처럼 다시 만들려고 join 씀




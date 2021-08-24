def solve(data):
    """
    ** 동작 과정 => 후위 표현식 연산과정 **
    1. 숫자는 stack에 넣는다.
    2. 연산자를 만나면 Stack에서 2개의 숫자를 꺼내 연산하고 그 결과를 다시 Stack에 넣는다.
    3. .은 코드의 끝을 의미하며 Stack에서 숫자를 꺼내 출력한다.
    """
    stack = []                                                                   # 연산 처리를 위한 stack 준비
    for i in range(len(data)):                                                   # data의 길이만큼 반복을 돌며
        if data[i] == '+' or data[i] == '-' or data[i] == '/' or data[i] == '*': # 만약에 연산자가 나오면
            if len(stack) >= 2:                                                  # stack에 2개 이상의 요소가 있는 경우에
                op2 = int(stack.pop())                                           # stack에서 숫자 2개를 꺼내고 +, -, *, / 연산진행
                op1 = int(stack.pop())
                if data[i] == '+':
                    stack.append(op1+op2)
                elif data[i] == '-':
                    stack.append(op1-op2)
                elif data[i] == '*':
                    stack.append(op1*op2)
                elif data[i] == '/':
                    stack.append(op1//op2)
            else:
                return 'error'                                                   # 만약 2개 이상의 요소가 없는 경우라면 연산을 하기 위한 피연산자가 부족하기 때문에 error
        elif data[i].isdigit():                                                  # 피연산자(숫자)인 경우는
            stack.append(data[i])                                                # 바로 stack에 push
        elif data[i] == '.':                                                     # .인 경우(마지막을 의미)
            if len(stack) == 1:                                                  # .을 만난 이후에 stack에 1개 남아있으면 이는 최종적으로 연산이 마무리된 피연산자(숫자)
                return stack.pop()                                               # 그 값을 반환
            else:                                                                # stack에 1개가 남아있지 않은 경우는 연산자가 부족하기 때문에 error!
                return 'error'
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    data = list(input().split())
    ans = solve(data)
    print('#{} {}'.format(tc, ans))

"""
예시)
| 5 |
| 3 |
|_1_|
위와 같은 Stack에서 피연산자를 뽑는 경우 
op2 -> 5
op1 -> 3
항상 순서는 op2가 뒤 op1가 앞 그리고 그걸 해당 연산자로 연산하는 과정
"""
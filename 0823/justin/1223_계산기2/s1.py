import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):      # 계산기2는 괄호 없는 버전
    N = int(input())
    data = input()
    stack = []               # 중위표기 -> 후위표기로 변경할 때 연산자 관리에 필요한 stack 준비
    new_data = []            # 새로운 계산식 (후위표기법)
    for c in data:           # 중위표기법으로 표현된 계산식을 하나씩 꺼내면서
        if c == '*':         # * 연산자를 만나면
            stack.append(c)  # 바로 stack에 넣고
        elif c == '+':       # + 연산자를 만나면
                                                        # (즉, + -> * 순으로 배치하기 위함 -> pop을 했을 때 *가 먼저 나올 수 있도록해야 연산자 우선순위 상 * 연산이 먼저 진행)
            while len(stack) != 0 and stack[-1] == '*': # stack이 비어있지 않고 stack의 가장 마지막이 *이 아닌 경우에
                new_data.append(stack.pop())            # 새로운 계산식에 stack에 있는 값을 pop하여 다 넣고
            stack.append(c)                             # + 연산자를 stack에 추가 (+의 우선순위가 더 낮기 때문)
        else:                                           # 만약 숫자라면 (어차피 숫자부터 만나게 됨)
            new_data.append(int(c))                     # 숫자로 변환하여 넣자
    for c in reversed(stack):                           # *를 +보다 먼저 넣어야 * 연산이 우선할 수 있음 (주의: reversed는 정렬아님)
        new_data.append(c)

    calculation = []                            # 최종 연산 결과를 담을 리스트
    for c in new_data:                          # 다시 꺼내어
        if c == '+':                            # 만약 +면
            second = calculation.pop()          # 2개 pop & 더하고
            first = calculation.pop()
            calculation.append(first + second)
        elif c == '*':                          # * 면
            second = calculation.pop()          # 2개 pop & 곱하고
            first = calculation.pop()
            calculation.append(first * second)
        else:                                   # 숫자면
            calculation.append(c)               # stack에 추가

    ans = calculation[0]
    print('#{} {}'.format(tc, ans))


"""
피연산자
- 0 ~ 9 
연산자
- *, +

1) 중위 표현식 -> 후위 표현식
ex) (6+5*(2-8)/2) -> 6528-*2/+

 - 피연산자가 나오면 그대로 출력
 - (이 나오면 stack에 push
 - *, /이 나오면 *과 /보다 우선순위가 높거나 같은 연산자면 stack에서 pop하여 붙이고 
   낮은 연산자를 만나면 stack에 push 
 - _, +가 나오면 -와 +보다 우선순위가 높거나 같은 연산자면 stack에서 pop하여 붙이고
   낮은 연산자를 만나면 stack에 push
 - 여는 괄호('(')의 경우 stack 안에서는 연산자 우선 순위가 가장 낮고 연산자 바깥에서는 우선순위가 가장 높음 
 -  닫는 괄호가 나오면 여는 괄호가 나올 때까지 stack에서 pop하여 출력하고 괄호는 버림

2) 후위 표현식 -> 계산
 - 6528-*2/+ -> -9

    2 - 8 = -6 
    5 * (-6) = -30 
    -30 / 2 = -15 
    6 + (-15) = -9

 - 피연산자가 나오면 stack에 push
 - 연산자를 만나면 연산에 필요한 만큼 피연산자를 stack에서 pop & 연산 수행 -> 연산 결과를 다시 stack에 push
 - 마지막 결과를 stack에서 pop
"""
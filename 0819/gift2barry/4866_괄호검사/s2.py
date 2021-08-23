import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(1, N+1):
    str_list = list(input()) # ['p','r']
    open_bracket = ['(', '{', '[']
    close_bracket = [')', '}', ']']
    stack = []
    j = 0
    while j < len(str_list):                  # str_list의 길이만큼 반복
        if str_list[j] in open_bracket:       # 만약 시작하는 괄호면
            stack.append(str_list[j])         # stack에 넣어줌
            j += 1
        elif str_list[j] in close_bracket:    # 닫히는 괄호면
            if len(stack) == 0:               # stack의 길이부터 확인
                stack.append('error')
                break                         # open_bracket의 인덱스와 close_bracket의 인덱스가 같으면
            elif close_bracket.index(str_list[j]) == open_bracket.index(stack[-1]):
                stack.pop(-1)                 # stack에서 빼버리기
                j += 1
        else:
            j += 1
    if len(stack) == 0:                       # while문이 끝났을 때 stack의 길이가 0이면 True
        stack = 1
    else:
        stack = 0                             # 아니면 False
    print('#{} {}'.format(i, stack))
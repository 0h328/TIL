import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = input()
    stack = []

    for char in data:       # data의 글자를 한글자씩 판단
        if not stack:       # stack 비어있으면 무조건 push
            stack.append(char)
        else:
            if stack[-1] == char:   # stack[-1]이 char와 같으면 연속 문자이므로
                stack.pop()         # pop으로 연속문자 제거
            else:
                stack.append(char)  # 연속문자 아니면 push

    ans = len(stack)                # 최종적으로 stack의 길이 출력
    print('#{} {}'.format(tc, ans))
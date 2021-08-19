import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    iron_bar = input()
    stack = []
    ans = 0

    for i in range(len(iron_bar)):
        if iron_bar[i] == '(':     # 여는 괄호라면
            stack.append('(')      # stack에 추가
        else:                      # 닫는 괄호면
            stack.pop()            # stack에서 꺼내고
            if iron_bar[i-1] == '(': # 그 전이 여는 괄호였다면
                ans += len(stack)    # stack에 남은 요소의 개수 더하기(레이저로 잘린 조각)
            else:
                ans += 1             # 닫는 괄호면 남는 조각 1개 추가
    print('#{} {}'.format(tc, ans))
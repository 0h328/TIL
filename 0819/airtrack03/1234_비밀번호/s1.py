import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N, data = input().split()
    N = int(N)
    stack = []

    for i in range(N):
        if stack:                       # 스택 비어있지 않으면
            if stack[-1] == data[i]:    # 스택의 마지막 값이 현재 인덱스의 data 값과 같으면 연속되므로 pop
                stack.pop()
            else:
                stack.append(data[i])   # 다르다면 push
        else:                           # 스택 비어있으면 무조건 push
            stack.append(data[i])

    ans = ''.join(list(map(str, stack)))    # 두 개가 연속된 수 제거된 stack 출력

    print('#{} {}'.format(tc, ans))
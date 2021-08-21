import sys

sys.stdin = open('input.txt')

T = int(input())
test_case = 1

while test_case <= T:
    brackets = input()

    cnt = 0
    stack = []

    for idx in range(len(brackets)):

        if brackets[idx] == '(':    # '('이면
            stack.append(0)         # 스택에 추가
        else:                       # ')'이면
            stack.pop()             # 스택에서 뽑아냄
            if brackets[idx-1] == brackets[idx]:    # )) 처럼 연속으로 나오면
                cnt += 1            # 쇠막대 하나의 길이 끝 => +1
            else:                   # () 처럼 나오면 => 레이저
                cnt += len(stack)   # 스택의 길이 = 쇠막대기 수 만큼 추가

    print('#{0} {1}'.format(test_case, cnt))
    test_case += 1

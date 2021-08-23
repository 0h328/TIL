import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    stack = []                                    # 문자 비교
    chars = input()                               # 문자 입력
    for i in range(len(chars)):                   # 문자열의 길이만큼 반복을 돌며
        if not len(stack):                        # stack이 비어 있으면
            stack.append(chars[i])                # 해당 문자 stack에 일단 추가
        else:                                     # stack이 비어있지 않을 때
            if stack[len(stack)-1] == chars[i]:   # 만약 stack의 마지막 인덱스(맨위)가 입력 문자의 i와 같다면(같은 문자라면)
                stack.pop()                       # stack에서 값을 꺼내고 (지우고)
            else:                                 # 같지 않으면 (다른 문자라면)
                stack.append(chars[i])            # stack에 추가
    ans = len(stack)
    print('#{} {}'.format(tc, ans))


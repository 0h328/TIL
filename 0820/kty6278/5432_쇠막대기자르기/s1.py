import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    iron = input()
    status = 0
    my_list = []

    for i in range(len(iron)):
        if iron[i] == '(':
            my_list.append(iron[i])  # stack-push    ( 가 나오는 경우 리스트에 무조건 추가
        elif iron[i] == ')':
            my_list.pop()            # stack-push    ) 이 나오는 경우 리스트에 마지막에 들어간 ( 제거 _ ()쌍 관련 ( 제거
            if iron[i - 1] == '(':   # ()인 경우 레이저로 잘린 경우
                status += len(my_list)
            else:
                status += 1             # ))인 경우 끝점이기에 전부 잘렸다면 나머지 부분 +1씩
    print('#{} {}'.format(tc + 1,status))

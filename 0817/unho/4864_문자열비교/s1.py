import sys
sys.stdin = open('input.txt')


test_case = int(input())

for tc in range(1, test_case+1):
    str1 = input().strip()
    str2 = input().strip()
    answer = 1

    if str2.find(str1) == -1:           # 포함되지 않으면 답을 0으로
        answer = 0

    print('#{} {}'.format(tc, answer))
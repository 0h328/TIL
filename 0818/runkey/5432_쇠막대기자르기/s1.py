import sys
sys.stdin = open('input.txt')

t = int(input())                    # 테스트 케이스 갯수
for tc in range(t):                 # 테스트 케이스 갯수만큼 반복
    print("#{0}".format(tc + 1), end=" ")    # 테스트 케이스 번호 출력

    case = list(input())
    result = 0
    result_list = []
    idx = 0
    for i in case:
        if i == '(':
            result_list.append(i)
            if case[idx + 1] == ')':
                result_list.pop()
                result += len(result_list)
                idx += 1
                continue
            idx += 1

        elif i == ')':
            if case[idx - 1] == '(':
                idx += 1
                continue

            elif case[idx - 1] == ')':
                result_list.pop()
                result += 1
                idx += 1
                continue
    print(result)


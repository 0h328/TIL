import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    num = int(input())
    print('#{}'.format(tc+1), end = '\n')

    new_list = [] # 배열 생성 리스트
    for i in range(num):
        case = [] # 새로운 덧셈 배열 생성 리스트
        for j in range(i + 1):
            if j == 0 or i == j:
                case.append(1)
            else:
                case.append(new_list[i-1][j-1] + new_list[i-1][j])
        new_list.append(case)

    for new in new_list:
        print(*new)
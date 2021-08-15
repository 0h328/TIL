import sys

# cp949 error without the parameter 'encoding'
sys.stdin = open('input.txt', 'rt', encoding='UTF-8')

test_case = 1
while test_case <= 10:
    int(input())    # 입력에 테스트 케이스 넘버가 있어서 제거
    patt = input()
    string = input()
    cnt = 0

    i = 0
    while i < len(string)-len(patt)+1:  # 마지막에 +1 추가

        j = 0
        while j < len(patt):
            # print(i, j)

            if patt[j] != string[i]:
                i -= j
                break
            i += 1
            j += 1
        else:
            i -= j
            cnt += 1

        i += 1

    print('#{0} {1}'.format(test_case, cnt))
    # break
    test_case += 1

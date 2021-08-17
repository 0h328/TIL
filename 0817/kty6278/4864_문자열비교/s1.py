import sys
sys.stdin = open('input.txt')

T = int(input())                   # testcase 받아오기
for tc in range(T):                # testcase 만큼 반복
    find_word = input()            # 찾아야 하는 문자열
    word = input()                 # 전체 문자열
    # print(find_word, word)
    if find_word in word:          # 찾아야 하는 문자열이 전체 문자열에 존재하는경우 1
        result = 1
    else:                          # 이외의 경우 0
        result = 0
    print('#{} {}'.format(tc + 1, result))
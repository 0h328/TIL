import sys

sys.stdin = open('input.txt', 'rt', encoding='UTF8')

for i in range(10):
    try_num = int(input())
    find_str = input()
    found_str = input()
    A = len(find_str)
    B = len(found_str)
    cnt = 0 # 일치한 횟수
    for z in range(B):
        cnt_test = 0 # 찾을 문자열의 길이가 일치하는지 확인하는 수단
        for k in range(A):
            if z + k < B: # 인덱스 초과를 방지위한 방법
                if find_str[k] != found_str[z + k]: # < 틀리다면 바로 멈춰서 z를 한글자 추가
                    break
                cnt_test += 1 # 맞다면 한번 더해주고 다시 돌림
                if cnt_test == (A): # 돌리다가 만약, 글자수와 같게된다면 cnt에 +1
                    cnt += 1
    print('#{} {}'.format(i + 1, cnt))

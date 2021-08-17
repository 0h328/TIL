'''
재귀로도 가능?
'''



import sys
sys.stdin = open('input.txt')


def find(string, m):
    for i in range(len(string)-m+1):
        tmp = string[i:i+m]             # 찾으려는 문자열 길이로 자름
        for j in range(len(tmp)//2):    # 문자열 앞뒤로만 비교하므로 길이의 반만큼만 반복
            if tmp[j] != tmp[-j-1]:     # 반대편 값 비교하다가 불일치하면 break
                break
        else:                           # 값이 모두 일치하면 반환
            return string[i:i+m]


test_case = int(input())

for tc in range(1, test_case+1):
    answer = ''
    n, m = map(int, input().split())
    str_list1 = [input().strip() for _ in range(n)]                                         # 가로
    str_list1.extend(list(map(lambda x: ''.join(x), map(list, zip(*str_list1)))))           # 세로

    for e in str_list1:
        tmp_answer = find(e, m)                                                             # 가로 검색

        if tmp_answer:                                                                      # 회문 있으면 정답에 저장
            answer = tmp_answer
            break

    print('#{} {}'.format(tc, answer))
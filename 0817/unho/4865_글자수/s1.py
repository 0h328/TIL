import sys
sys.stdin = open('input.txt')


test_case = int(input())

for tc in range(1, test_case+1):
    str1 = input().strip()
    str2 = input().strip()
    counted = []
    answer = []

    for c in str1:
        if c not in counted:                        # 이미 확인한 문자이면 카운트 생략
            answer.append([c, str2.count(c)])       # 정답 배열에 해당 문자와 갯수를 리스트 형태로 넣음
            counted.append(c)

    answer.sort(key=lambda x: x[1], reverse=True)   # 갯수를 기준으로 내림차순 정렬

    print('#{} {}'.format(tc, answer[0][1]))
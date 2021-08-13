import sys
sys.stdin = open('input.txt')



order = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']  # 문자열의 순서들

test_case = int(input())

for tc in range(1, test_case+1):
    trash = input()

    number = {}                                     # 숫자에 해당하는 문자열이 나오는 갯수 카운트
    answer = []                                     # 트답 리스트

    for e in input().split():                       # 입력받은 리터럴 문자들을 딕셔너리에서 해당 문자열 키값에 +1
        number[e] = number.get(e, 0) + 1

    for e in order:                                 # 문자열의 순서에 맞게 요소를 가져와서 나온 갯수만큼 정답 리스트에 할당
        answer.extend([e] * number.get(e, 0))

    print('#{} {}'.format(tc, ' '.join(answer)))
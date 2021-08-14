import sys
sys.stdin = open('input.txt')

# 소요시간: 32분 31초

# thought process:
# 인풋값을 공백을 기준으로 각 문자열들을 나누어 리스트안에 저장
# ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN'] 루프 돌리며 해당 문자열 전부 카운트
# 새로운 리스트에 해당 단어만큼 append 해서 저장
# 새로운 리스트를 문자열로 합쳐서 프린트


T = int(input())
for tc in range(1, T+1):
    tc_index, str_num = map(str, input().split())

    arr = list(map(str, input().split()))

    ordered = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN'] # 문자열 순서대로 배치

    ordered_list = []                       # 정돈 된 문자열 보관용 리스트 생성

    for i in ordered:                       # 차례대로 정돈된 문자열 접근
        cnt = 0                             # 찾는 문자열의 개수 카운터 초기화
        for j in arr:                       # 인풋 arr 안에서 정돈된 문자열 탐색
            if i == j:                      # 처음 한개 찾으면
                cnt = arr.count(j)          # 전체 arr에서 동일한 문자열 개수 카운트
                break                       # 현재 루프 강제 종료하고, 다음 정돈된 문자열 탐색 ㄱ
        ordered_list += ([i] * cnt)         # 마지막 루프에서 찾은 문자열을 카운트 개수만큼 저장 (2차원 리스트 생성 필요x, 고로 append 사용안함)

    ans = ' '.join(ordered_list)            # ordered_list를 하나의 문자열로 합쳐서
    print('{}\n{}'.format(tc_index, ans))   # 프린트

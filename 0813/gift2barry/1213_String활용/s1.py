import sys
import time
sys.stdin = open('input.txt', encoding='UTF-8')

start_time = time.time()
# thought process:
# 무어 알고리즘 구현해보려 노력
# 패턴의 끝부분 비교
# 틀리면 패턴의 뒤에 문자를 순차적으로 비교
# 있으면 일치된 인풋문자열인덱스 - 패턴문자열인덱스 만큼 앞으로 패턴문자열 이동하고 패턴의 끝부분 비교
# 만약 일치되는 문자 없으면, 패턴 문자열 길이만큼 이동

# for tc in range(1, 11):
#
#     tc_idx = int(input())   # 테스트 케이스 넘버링
#     pattern = list(input()) # 패턴문자열 인풋
#     p = len(pattern)
#     arr = list(input())     # 문자열 인풋
#     i = 0                   # 문자열의 위치 index 초기화
#     cnt = 0                 # 찾은 패턴문자열 개수 초기화
#     while i < len(arr):
#         if pattern[p-1] == arr[i+p-1]:

# 소요시간 약 3분
for tc in range(1, 11):
    tc_idx = input()
    pattern = input()
    arr = input()
    num = arr.count(pattern)
    print('#{} {}'.format(tc_idx, num))
print("--- %s seconds ---" % (time.time() - start_time))

# 수민님 코드 참고
for _ in range(1, 11):
    tc = int(input())
    pattern = input()  # 찾을 문자열
    sentence = input()   # 검색할 문장

    P = len(pattern)   # 찾을 문자열 길이
    S = len(sentence)    # 검색할 문장의 길이

    j = 0  # 찾을 문자열의 인덱스
    i = 0  # 검색할 문장의 인덱스
    cnt = 0  # 개수

    while i < S and j < P:
        if sentence[i] == pattern[j]:  # 문장의 문자와 패턴의 문자가 같으면 1씩 더해서 다음 인덱스값 비교
            i += 1
            j += 1
        else:  # 같지 않으면 문장의 인덱스는 같지 않은 곳으로, 패턴 인덱스는 처음으로
            i = i - j + 1
            j = 0
        if j == P:  # 패턴의 마지막까지 비교하여 같으면 개수 하나 더하고 패턴의 인덱스는 처음으로
            cnt += 1
            j = 0

    print('#{} {}'.format(tc, cnt))


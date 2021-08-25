import sys
sys.stdin = open("input.txt", encoding='UTF8')

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
        else:                          # 같지 않으면
            i = i - j + 1              # 문장의 인덱스는 같지 않은 곳으로
            j = 0                      # 패턴 인덱스는 처음으로
        if j == P:                     # 패턴의 마지막까지 비교하여 같으면
            cnt += 1                   # 개수 하나 더하고
            j = 0                      # 패턴의 인덱스는 처음으로

    print('#{} {}'.format(tc, cnt))






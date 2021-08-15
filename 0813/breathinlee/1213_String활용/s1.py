import sys
sys.stdin = open("input.txt", encoding='UTF8')

for _ in range(1, 11):
    tc = int(input())
    pattern = input()  # 찾을 문자열
    sentence = input()   # 검색할 문장

    M = len(pattern)   # 찾을 문자열 길이
    K = len(sentence)    # 검색할 문장의 길이

    j = 0  # 찾을 문자열의 인덱스
    i = 0  # 검색할 문장의 인덱스
    cnt = 0  # 개수

    while i < K and j < M:
        if sentence[i] == pattern[j]:  # 문장의 문자와 패턴의 문자가 같으면 1씩 더해서 다음 인덱스값 비교
            i += 1
            j += 1
        else:  # 같지 않으면 문장의 인덱스는 같지 않은 곳으로, 패턴 인덱스는 처음으로
            i = i - j + 1
            j = 0
        if j == M:  # 패턴의 마지막까지 비교하여 같으면 개수 하나 더하고 패턴의 인덱스는 처음으로
            cnt += 1
            j = 0

    print('#{} {}'.format(tc, cnt))






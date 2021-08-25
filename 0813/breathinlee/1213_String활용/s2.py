import sys
sys.stdin = open("input.txt", encoding='UTF8')

for _ in range(1, 11):
    tc = int(input())
    pattern = input()  # 찾을 문자열
    sentence = input()   # 검색할 문장

    P = len(pattern)  # 찾을 문자열 길이
    S = len(sentence)  # 검색할 문장의 길이
    cnt = 0

    for i in range(S-P+1):    # 어디서 많이 본 코드 => 구간합 / 파리퇴치
        for j in range(P):
            if sentence[i+j] != pattern[j]:
                break
        else:
            cnt += 1
    print('#{} {}'.format(tc, cnt))
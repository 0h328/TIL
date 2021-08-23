import sys
sys.stdin = open('input.txt')


test_case = int(input())

for tc in range(1, test_case+1):
    str1, str2 = input().split()
    answer = 0

    idx = 0                                     # 시작 인덱스
    while idx < len(str1):                      # 긴 문자열 인덱스까지
        answer += 1                             # 문자 하나 카운트
        if str1[idx:idx+len(str2)] == str2:     # 현재 인덱스부터 두번째 문자열 인덱스 길이만큼 슬라이싱 / 두번째 문자열과 같으면
            idx += len(str2)                    # 두번째 문자열 길이만큼 점프
            continue
        idx += 1                                # 두번째 문자열과 다르면 인덱스 1만 증가

    print('#{} {}'.format(tc, answer))
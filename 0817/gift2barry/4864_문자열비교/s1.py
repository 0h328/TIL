import sys
sys.stdin = open('input.txt')
# 소요시간: 29분

# thought process
# 고지식 알고리즘으로 풀어보자
# 패턴 문자열과 전체 문자열 대조,
# 동일하면 둘 다 한칸씩 인덱스 전진하고 대조,
# 틀리면 패턴 문자열 인덱스값 초기화, 전체 문자열 = 전체 - 패턴문자열 + 1
# 패턴 문자열 카운터가 패턴 문자열의 길이에 도달하면 숫자 1 반환
# 패턴 문자열 카운터가 패턴 문자열의 길이에 도달하기 전에 루프가 끝나면 0 반환

T = int(input())
for tc in range(1, T+1):
    pattern = input()   # 검색 문자열
    arr = input()       # 전체 문자열
    P = len(pattern)    # 검색 문자열 길이
    A = len(arr)        # 전체 문자열 길이

    i = 0   # 검색 문자열 idx
    j = 0   # 전체 문자열 idx

    while i < P and j < A:
        if pattern[i] == arr[j]:        # 패턴 문자열과 전체 문자열 대조
            i += 1                      # 동일하면 둘 다 한칸씩 인덱스 전진하고 대조 반복
            j += 1
        else:                           # 틀리면
            j = j - i + 1               # 전체 문자열idx = 전체문자열idx - 패턴문자열idx + 1
            i = 0                       # 패턴 문자열 인덱스값 초기화
        if i == P:                          # 패턴 문자열 카운터가 패턴 문자열의 길이에 도달하면
            print('#{} {}'.format(tc, 1))   # 숫자 1 반환
    if i != P:                              # 패턴 문자열 카운터가 패턴 문자열의 길이에 도달하기 전에 루프가 끝나면
        print('#{} {}'.format(tc, 0))       # 0 반환

    # if pattern in arr:
    #     print(1)
    # else:
    #     print(0)







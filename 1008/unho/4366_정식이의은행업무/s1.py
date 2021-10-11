import sys
from collections import deque
sys.stdin = open('input.txt')


def decimal_to_triple(num):                 # 십진수를 3진수로 변형
    result = deque()

    while num:
        result.appendleft(str(num % 3))
        num //= 3
    
    while len(result) < M:                  # 기존 3진수보다 자릿수 부족시 앞에 0으로 채움
        result.appendleft('0')

    return result


T = int(input())
answer = []

for tc in range(1, T+1):
    default_bin = input()                   # 기존 2진수, 3진수
    default_triple = input()

    N = len(default_bin)                    # 각 진수별 길이수
    M = len(default_triple)

    default_bin = int(default_bin, 2)       # 10진수 숫자형으로 변환

    idx = 0                                 # 2진수의 1의 자리부터 차례대로 하나씩 값 변경 반복하는 로직
    while idx < N:
        default_bin ^= 1 << idx                         # 값 스위치
        converted = decimal_to_triple(default_bin)      # 현재 2진수 값 3진수로 변형

        cnt = 0
        for i in range(M):                              # 바뀐 3진수와 기존 3진수가 몇글자가 바뀌었는지 카운트
            if default_triple[i] != converted[i]:
                cnt += 1
        
        if cnt == 1:                                    # 3진수 하나만 바꿔도 된다면 정답으로 저장
            answer.append('#{} {}'.format(tc, default_bin))
            break

        default_bin ^= 1 << idx         # 값 복구
        idx += 1                        # 다음 자릿수
        
print(*answer, sep='\n')
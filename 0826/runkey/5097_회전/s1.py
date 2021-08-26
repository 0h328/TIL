import sys
sys.stdin = open('input.txt')

t = int(input())                                # 테스트 케이스 갯수
for tc in range(1, t + 1):                      # 테스트 케이스 갯수
    N, M = map(int, input().split())            # N, M에 숫자 갯수와 이동 수를 입력
    temp = list(map(int, input().split()))      # temp에 N개의 숫자들을 넣어줌
    result = temp[M % N]                        # result에 N을 M으로 나눈 나머지 값의 인덱스를 temp에서 가져옴
    print("#{} {}".format(tc, result))          # 출력
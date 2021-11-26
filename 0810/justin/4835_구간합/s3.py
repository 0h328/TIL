import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    """
    컨셉 ->  중복 연산을 줄이자 
    첫 구간의 합을 구해 놓고 
    -> 다음 구간은 첫 구간에서 가장 앞 인덱스를 빼고 
    -> 현재 구간에서 가장 뒷 인덱스를 더한다.
    """

    tmp = 0
    for i in range(M):           # 첫 구간은 전체 합이 무조건 필요 (M-1)까지
        tmp += numbers[i]

    max_value = min_value = tmp  # 가장 처음 tmp 값으로 초기화

    for i in range(M, N):       # 다음 구간 부터는 M부터 N-1까지
        # numbers[i-M] -> 이전 구간합에 포함되어 중복된 원소
        # numbers[i] -> 추가되는 원소
        # 새로운 구간의 합을 간단하게 구현 가능
        """
        1 2 3 4 5 6 7 8 9 10
        1. 1 + 2 + 3 -> 6
        2. 4(인덱스3) - 1(인덱스0) -> 3 -> 기존 구간합에서 3만큼 더 크다는 의미 
        """
        tmp += numbers[i] - numbers[i-M]

        # 최대 & 최소 구하기
        if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp
    ans = max_value - min_value
    print('#{} {}'.format(tc, ans))

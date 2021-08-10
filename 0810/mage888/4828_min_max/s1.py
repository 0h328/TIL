import sys
sys.stdin = open('input.txt')
                                                   # 입력받은 숫자의 가장 큰 수와 작은 수의 차이를 구하기 위한 문제.
T = int(input())                                   # 테스트 케이스 개수

for test_case in range(1, T+1):                    # 자료받은 개수를 테스트 케이스만큼 돌리기.
    N = int(input())                               # N = 자료의 개수 (= 길이)
    numbers = list(map(int,input().split()))       # 자료를 list로 받기 위해 numbers라는 변수 생성.

    max_value = numbers[0]
    min_value = numbers[0]
    # max_value = min_value = numbers[0]
                                                   # 구하고자하는 가장 큰 수, 가장 작은 수를 list 내 임의 요소로 초기화
    result = 0                                     # result는 최댓값과 최솟값의 차이를 구하기 위해 0으로 초기화하여 설정
    for number in numbers:                         # numbers list를 순환하기 위해 for문 작성
        if max_value < number:                     # list 내 요소가 초기화한 변수보다 작으면
            max_value = number                     # 해당 요소를 max_value에 갱신

        if min_value > number:                     # list 내 요소보다 초기화한 변수가 크면
            min_value = number                     # 해당 요소를 min_value에 갱신

        result = max_value - min_value             # 각 list 내 최댓값과 최솟값을 빼서 result에 저장

    print('#{} {}'.format(test_case, result))



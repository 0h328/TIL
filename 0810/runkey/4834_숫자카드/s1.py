import sys
sys.stdin = open("input.txt")           # 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램
                                        # 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력
t = int(input())                        # 테스트 케이스 갯수

for tc in range(1, t + 1):              # 테스트 케이스 갯수만큼 반복
    number = [0 for _ in range(10)]     # 0을 10개 채운 number라는 list 생성
    card_count = int(input())           # 쓰지는 않지만, input()을 받기에 써줌.

    for i in input():                   # 입력값이 string이기에 숫자 하나씩 받음
        number[int(i)] += 1             # 정수로 형변환해서 해당 인덱스에 1을 더해줌

    result_value = max(number)          # 가장 큰 값을 result_value에 저장

    for j in range(len(number) - 1, -1, -1):    # number 리스트를 역순으로 돌림
        if number[j] == result_value:           # number의 해당 인덱스 값이 result_value랑 같으면
            result_idx = j                      # result_idx에 해당 인덱스 값을 넣어줌
            break                               # break로 반복문 빠져나옴
    print("#{2} {1} {0}".format(tc, result_idx, result_value))
    print("#{0} {1} {2}".format(tc, result_idx, result_value))
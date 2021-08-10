import sys
sys.stdin = open('input.txt')
                                                # 가장 많은 카드에 적힌 숫자와 카드가 몇장 ? = 입력 받은 숫자 중 가장 많이 입력받은 숫자의 개수와 그 숫자가 무엇인지 출력하는 문제
T = int(input())                                # 테스트 케이스 입력

for test_case in range(1, T+1):                 # 자료받은 개수를 테스트 케이스만큼 돌리기.
    N = int(input())                            # N = 자료의 개수 (= 길이)
    number = input()                            #list(map(int, list(input()))) #split 사용시 -> [ 입력예시 ]

    mv = number[0]                              # max_value의 약자인 mv를 리스트 내 아무 요소로 초기화
    for nb in number:                           # number list를 순환
        if mv < nb:                             # number list 내 큰 수 비교
            mv = nb                             # 갱신

    counts = [0] * (int(mv)+1)                  # counts 리스트 [0, 0, ... , 0, 0] 을 만든 이유는?

    for i in number:
        counts[int(i)] += 1                     # list 내 입력된 자료값이 해당하는 위치에 1씩 더해줌. [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]

    ans_idx = 0                                 # 입력받은 숫자는 counts list 내 index에 위치하기때문에 초기화.
    max_value = counts[0]                       # counts list 내 최댓값을 구하기 위해 요소 중 하나를 초기화 / list 내 value는 입력받은 숫자의 개수!

    for idx, val in enumerate(counts):          # enumerate를 통해서 idx와 val 값을 순환시키는 for문을 작성.
        if max_value <= val:                    # list 내 입력받은 숫자의 개수가 큰 값을 출력하기 위해 and 개수가 같을 경우엔 가장 큰 index를 출력하기 위해
            ans_idx, max_value = idx, val       # 초기화 시킨 idx(입력받은 숫자)와 val(입력받은 숫자의 개수)를 출력

    print('#{} {} {}'.format(test_case, ans_idx, max_value))
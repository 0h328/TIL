import sys
sys.stdin = open('input.txt')

for t in range(1, 11):  # 테스트 케이스 10번 반복
    tc = input()        # 테스트 케이스 번호
    temp_list = list(map(int, input().split())) # temp_list 에 input 값을 공백 기준으로 나눠서 리스트로 받음
    temp = 0            # temp는 맨 뒤에 들어가는 값
    stack = list()      # temp_list 복사본 들어가는 곳
    result = ''         # 결과 값

    while temp_list[-1] > 0:            # temp_list 끝에가 0 초과일 때만 반복
        for i in range(1, 6):           # 1 사이클
            stack = temp_list[1:]       # stack에 temp_list의 인덱스1 부터 끝까지 복사
            temp = temp_list[0] - i     # temp에 0번째 인덱스에서 i를 뺀 값을 넣음
            if temp < 0:                # temp가 음수이면
                temp = 0                # temp를 0으로 만듦
            stack.append(temp)          # stack에 temp를 추가함
            temp_list = stack[:]        # temp_list에 stack을 복사함
            if temp_list[-1] == 0:      # temp_list 마지막이 0이면
                break                   # 반복문 탈출 멈...멈춰!

    while temp_list:                    # temp_list가 빌 때까지
        result += str(temp_list.pop(0)) # result에 temp_list의 처음을 pop해서 str로 변환해서 더함
        result += ' '                   # result에 공백 추가
    print("#{} {}".format(t, result))   # 출력
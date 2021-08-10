import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    toNM = list(map(int,input().split())) #N,M을 따로 뽑아내기위하여 하나의 리스트 생성
    N = toNM[0] # 그 안에서 N과 M의 갯수 추출(N은 받아오는 갯수, M은 합할 갯수)
    M = toNM[1]
    Numbers = list(map(int,input().split())) # Numbers안에 받아올 숫자들을 리스트로 저장
    for k in range(N-M+1): # range의 범위 이유는 list 참조값을 넘지 않고, 더할것을 고려하여 설정
        temp_ans = 0
        M = toNM[1] # > M을 한번더 설정해주는 이유 > while문을 돌리는데 M의 숫자를 줄여가며 하기 때문에 다시한번 설정
        if k == 0: # > K가 0일때 새로 설정해준 이유 : min값과 max값을 한번 초기화시켜주기 위하여(모두 음수일경우 고려)
            while M > 0:
                temp_ans += Numbers[k+M-1] # > 앞에서부터가 아닌 while문을 활영화여 뒤에서부터 합)
                M -= 1
            min_ans = max_ans = temp_ans
        else:
            while M > 0:
                temp_ans += Numbers[k+M-1]
                M -= 1
            if temp_ans > max_ans:
                max_ans = temp_ans
            elif temp_ans < min_ans:
                min_ans = temp_ans

    print('#{} {}'.format(i+1,max_ans-min_ans))






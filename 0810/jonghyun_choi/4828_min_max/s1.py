import sys
sys.stdin = open('input.txt')

T = int(input()) # 테스트 케이스 갯수

for case in range(T):
    N = int(input())  # 양수의 갯수
    a = list(map(int,input().split()))
    min_num = a[0]    # min_num, max_num a의 첫 인덱스 값으로 초기화
    max_num = a[0]
    for number in a:
        if number > max_num:    # a를 순회하면서 요소가 max_num 보다 크면 max_num를 업데이트
            max_num = number
        if number < min_num:    # a를 순회하면서 요소가 min_num 보다 작으면 min_num를 업데이트
            min_num = number
    res = abs(max_num-min_num)  # max_num 과 min_num의 gap을 res에 저장

    print('#{} {}'.format(case+1,res))



import sys
sys.stdin = open('input.txt')

N = int(input())

for idx in range(1, N + 1):                     #함수로 구현하려고 했지만, 이런 light한 문제는 굳이 함수 없이 구현하는 것도 GOOD
    M = int(input())
    numbers = list(map(int, input().split()))   #여기서 이차원 행렬로 불러와서 계속 오류 발생했었음

    maxi = numbers[0]                           #max_my 이런거 말고 maximum의 약자 maxi를 사용하는 것 편해보여서 따라함
    mini = numbers[0]

    for i in range(M-1):                        #인덱스를 고려하여 M-1로 설정
        if numbers[i+1] > numbers[i]:           #더 크면 maxi에 저장, 작으면 maxi에 저장
            maxi = numbers[i+1]
        if numbers[i+1] < numbers[i]:           #습관적으로 else문 쳤다가 오류 발 생, if로 해야지 얘도 들어갔다가 나옴
            mini = numbers[i+1]
        ans = maxi - mini                       #차이 저장

    print('#{} {}'.format(idx, ans))



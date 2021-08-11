import sys
sys.stdin = open('input.txt')

tc = int(input())
for _ in range(tc):
    test_list = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    result_list = []
    for i in range(test_list[0]-test_list[1]+1):   # 숫자카드를 순서대로 n개 더할 횟수 구하기
        result = 0
        for j in range(i,i+test_list[1]):          # 더할 횟수 만큼 반복
            result += num_list[j]
        result_list.append(result)                 # result_list에 더한 숫자 넣기

    print('#{0} {1}'.format(tc, max(result_list)-min(result_list))) # result_list에서 가장 큰 수 - 가장 작은 수의 값 출력

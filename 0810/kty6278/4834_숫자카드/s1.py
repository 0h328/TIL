import sys
sys.stdin = open('input.txt')

# 테스트 케이스를 받아온다.
T = int(input())
# 테스트 케이스에 맞는 정수의 개수 n 과 구간의 개수 m 그리고 정수 ai를 받는 'numbers'를 받아온다.
for t in range(T):
    n = int(input())
    numbers = list(map(int, input()))
    #print(numbers)

    # 새롭게 리스트를 0 으로 쌓아주고
    my_list = [0] * 10
    # 숫자가 'numbers'에 존재하는 경우 +1 씩 더해준다.
    for i in range(n):
        my_list[numbers[i]] += 1

    # 최대의 값을 설정하고
    max_value = 0
    print(my_list)
    # 'enumerate'를 사용해서 'idx'와 'count'를 통해 'max_value'와 비교해준다.
    for idx, count in enumerate(my_list):
        if count >= max_value:
            max_value = count
            max_idx = idx
    print('#{} {} {}'.format(t+1, max_idx, max_value))
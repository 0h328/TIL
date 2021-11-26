import sys

sys.stdin = open('input.txt')

for test in range(1, 11):
    N = int(input())

    data = list(map(int, input().split()))

    while data[-1] > 0: # 마지막이 0이 아닐때까지 반복
        for i in range(1, 6):
            first = data.pop(0) # 첫번째 값을 뽑아서
            if first - i <= 0: # 둘의 차이가 0이거나 작으면
                data.append(0) # 0을 뒤에 더해주고
                break # 정지
            data.append(first - i) # 아닌경우에는 그 값을 더해준다

    print('#{}'.format(test), *data)

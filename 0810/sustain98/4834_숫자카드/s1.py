import sys
sys.stdin = open('input.txt')

t = int(input())

for idx in range(1, t+1):
    n = int(input())
    num_list = [int(i) for i in input().strip()]        # 입력받은 숫자들을 한 요소씩 자르고 int로 변환하여 list에 넣어준다.
    cnt_list = [0]*10                                   # 0-9까지 숫자의 카운트를 value로 가지게될 list생성
    for s in range(10):
        cnt_list[s] = num_list.count(s)                 # 0-9까지 숫자로 각각 num_list에서 갯수를 센다.

    max_idx = 0
    for i in range(1, 10):
        if cnt_list[max_idx] <= cnt_list[i]:            # 등호를 이용해 맨 뒤쪽에 있는 가장 큰 값의 idx가 max_idx에 오도록 함
            max_idx = i

    print('#{} {} {}'.format(idx, max_idx, cnt_list[max_idx]))


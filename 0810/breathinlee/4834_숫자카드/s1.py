import sys
sys.stdin = open("input.txt")

N = int(input())                                      # 케이스의 개수 가져오기
for tc in range(1, N + 1):
    num = int(input())                                # 카드 장수
    numbers = input()                                 # 카드에 적힌 숫자
    cnt_nums = [0] * 10                               # 숫자는 0 ~ 9까지 이므로 0 ~ 9 까지의 인덱스를 갖는 리스트 생성

    for i in range(num):
        cnt_nums[int(numbers[i])] += 1                # 카드에 적힌 숫자를 인덱스로 하는 자리에 1씩 더해줌

    max_cnt = max(cnt_nums)                           # cnt_nums의 값 중 최댓값을 max_cnt로 저장

    # if cnt_nums.count(max_cnt) > 1:                 # 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력해야 함
    cnt_nums.reverse()                                # reverse를 활용하여 리스트를 역순으로 출력
    max_card = 9 - cnt_nums.index(max_cnt)            # 역순이기 때문에 처음의 index를 구하기 위해 9에서 그 index 값을 빼줌
    # else:
    #     max_card = cnt_nums.index(max_cnt)          # 그 외는 가장 큰 값의 index를 출력
    print('#{} {} {}'.format(tc, max_card, max_cnt))
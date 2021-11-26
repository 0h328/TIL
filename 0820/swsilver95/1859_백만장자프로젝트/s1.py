import sys

sys.stdin = open('input.txt')

T = int(input())
d = []
datum = []
for _ in range(T):
    d.append(int(input().rstrip()))
    datum.append(list(map(int, input().split(' '))))


def money(total, my_list):                                  # 리스트 사재기 (재귀)
    if len(my_list) <= 1:                                   # 리스트 길이가 1 이하가 되면
        return total                                        # 수익금을 리턴 

    earn = total                                            # 현재 수익을 earn으로 초기화
    price_max = max(my_list)                                # 최대값을 찾은 다음
    idx = my_list.index(price_max)                          # 최대 수익이 되는 시기를 인덱스로 찾고
    buy_list = my_list[:idx + 1]                            # 최대가 나타나는 지점까지 슬라이싱
    # print(buy_list)
    earn += len(buy_list) * price_max - sum(buy_list)       # 수익금은 넓이로 생각
    # print(earn)
    if len(buy_list) == len(my_list):                       # 만약 끝까지 슬라이싱이 됐다면
        return earn                                         # 수익을 반환
    else:
        return money(earn, my_list[idx + 1:])               # 그렇지 않다면 재귀호출


for i in range(T):
    print('#{} {}'.format(i+1, money(0, datum[i])))
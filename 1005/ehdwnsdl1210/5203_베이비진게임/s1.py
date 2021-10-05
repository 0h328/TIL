'''
0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때,
연속인 숫자가 3개 이상이면 run
같은 숫자가 3개 이상이면 triplet

게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져가며,

6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자!!!
두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때, 승자는?
무승부인 경우 0을 출력

예를 들어 9 9 5 6 5 6 1 1 4 2 2 1인 경우,
플레이어 1은 9, 5, 5, 1, 4, 2카드를,
플레이어2는 9, 6, 6, 1, 2, 1을 가져가게 된다.
이때는 카드를 모두 가져갈 때 까지 run이나 triplet이 없으므로 무승부가 된다.
'''

def Run(number):        # 연속인 숫자가 3개 이상
    for i in range(max(number), 1, -1):     # 굳이 9부터 X 젤 큰거 부터 ~ 2까지만 (2면 2,1,0)
        if i in number and i-1 in number and i-2 in number:     # 안에 있으면 Good
            return True

    return False

def Triplet(number):        # 같은 숫자가 3개 이상
    number.sort()           # 정렬 하고
    for i in range(len(number) - 2):        # 3개 이상이니까 (3개면 1만 보면되고, 4매면 1,2만 보면 되고...)
        if number.count(i) >= 3:            # 3개이상 Good
            return True

    # for i in range(max(number) + 1):
    #     if number.count(i) >= 3:
    #         return True
    return False


import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    card = tuple(map(int, input().split()))
    number_1 = []       # 1 친구 담을거
    number_2 = []       # 2 친구 담을거

    for i in range(len(card)):      # 순회
        if i % 2:                   # 홀 인덱스는 2
            number_2.append(card[i])
            if len(number_2) >= 3:      # 1, 2개는 볼 필요 X
                if Run(number_2):
                    print('#{} {}'.format(tc, 2))
                if Triplet(number_2):
                    print('#{} {}'.format(tc, 2))

        else:                       # 짝 인덱스(0부터)는 1
            number_1.append(card[i])
            if len(number_1) >= 3:
                if Run(number_1):
                    print('#{} {}'.format(tc, 1))
                if Triplet(number_1):
                    print('#{} {}'.format(tc, 1))

    if any([Run(number_1), Run(number_2), Triplet(number_1), Triplet(number_2)]) != True:       # 하나라도 True면 True 반환 (any)
        print('#{} {}'.format(tc, 0))       # 무승부
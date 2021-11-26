'''
두 명의 손님에게 음식을 제공
두 명의 손님은 식성이 비슷, 최대한 비슷한 맛의 음식을 만들어 내야 한다.
N개의 식재료가 있다.
식재료들을 각각 (N / 2)개씩 나누어 두 개의 요리를 하려고 한다. (N은 짝수이다.)
이때, 각각의 음식을 A음식, B음식
비슷한 맛의 음식을 만들기 위해서는 A음식과 B음식의 맛의 차이가 최소가 되도록 재료를 배분
음식의 맛은 음식을 구성하는 식재료들의 조합에 따라 다름


식재료 i는 식재료 j와 같이 요리하게 되면 궁합이 잘 맞아
시너지 Sij가 발생(1 ≤ i ≤ N, 1 ≤ j ≤ N, i ≠ j)
각 음식의 맛은, 음식을 구성하는 식재료들로부터 발생하는 시너지 Sij들의 합


식재료 i를 식재료 j와 같이 요리하게 되면 발생하는 시너지 Sij의 정보가 주어지고,
가지고 있는 식재료를 이용해 A음식과 B음식을 만들 때,
두 음식 간의 맛의 차이가 최소가 되는 경우를 찾고
그 최솟값을 정답으로 출력하는 프로그램을 작성

(세로축으로 i번째 위치에 있고 가로축으로 j번째 위치에 있는 값이 Sij이다.)

식재료의 수 N은 4이상 16이하의 짝수이다. (4 ≤ N ≤ 16)
시너지 Sij는 1이상 20,000이하의 정수이다. (1 ≤ Sij ≤ 20,000, i ≠ j)
i와 j가 서로 같은 경우의 Sij값은 정의되지 않는다. 입력에서는 0으로 주어진다.
'''

from pandas import DataFrame
from itertools import combinations      # 딴건 모르겠고, 조합으로 감
                                        # itertools 못쓰면, 동완님 코드!?!
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())        # 반띵씩 사용(A, B)
    synergy = [list(map(int, input().split())) for _ in range(N)]
    # print(DataFrame(synergy))

    flavor_difference = 40000       # 최소 값을 구할 기준! (최대 40000 - 2)

    ingredients_num = {n for n in range(N)}     # 식재료 idx
    # print(ingredients_num)

    half_ingredient_num = combinations(ingredients_num, N//2)       # 반띵 가능 수
    # print(set(half_ingredient_num))

    # 여기서(바로 밑 for문만) 과정이 좀 길어지는데, 교집합이 없는애라는 조건을 통해서 단축 가능할란가
    for i in half_ingredient_num:
        flavor_sum_1 = 0        # 앞 친구 시너지 합
        flavor_sum_2 = 0        # 뒷 친구 시너지 합
        ingredients_1 = set(i)
        ingredients_2 = set(ingredients_num) - set(i)       # 이 과정을 위해 일단 집합으로 표현 (앞 아닌건 뒤이므로)
        # print(ingredients_1, ingredients_2)

        for j in range(len(ingredients_1) - 1):       # 완전 탐색(?) / 다 살펴보는거
            for k in range(j + 1, len(ingredients_1)):
                flavor_sum_1 += synergy[list(ingredients_1)[j]][list(ingredients_1)[k]]     # set은 순서가 없어서, list로 변환
                flavor_sum_1 += synergy[list(ingredients_1)[k]][list(ingredients_1)[j]]

                flavor_sum_2 += synergy[list(ingredients_2)[j]][list(ingredients_2)[k]]     # 뒷 친구도 앞 친구랑 판박이
                flavor_sum_2 += synergy[list(ingredients_2)[k]][list(ingredients_2)[j]]

        if flavor_difference > abs(flavor_sum_1 - flavor_sum_2):        # 최소 비교
            flavor_difference = abs(flavor_sum_1 - flavor_sum_2)

    print('#{} {}'.format(tc, flavor_difference))

'''
#1 2
#2 1
#3 38
#4 15
#5 4
#6 0
#7 51
#8 23
#9 13
#10 11
'''
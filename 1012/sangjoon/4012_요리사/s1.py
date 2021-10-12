# 1. 문제 솔루션 코드를 작성합니다.
from itertools import combinations

# 클래스명이 마음에 들지 않습니다.


class Cook:
    def __init__(self, food_synergy, total_food):
        self.food_synergy = food_synergy
        self.total_food = total_food

        # 음식 조합의 시너지를 구하는 함수
    def get_synergy(self, food_lst):
        synergy = 0

        for a, b in combinations(food_lst, 2):
            synergy += self.food_synergy[a][b] + self.food_synergy[b][a]

        return synergy

        # 음식 리스트를 분리하는 로직이 아래의 코드보다 더 좋겠다는 생각을 했습니다.
    def get_min_synergy(self):
        food_lst = [i for i in range((self.total_food))]
        min_synergy = float("inf")

        for food_a in combinations(food_lst, self.total_food//2):
            food_b = set(food_lst) - set(food_a)
            min_synergy = min(min_synergy, abs(
                self.get_synergy(food_a)-self.get_synergy(food_b)))

        return min_synergy


test_case = int(input())
for test in range(1, test_case+1):
    n = int(input())
    gh = [list(map(int, input().split())) for _ in range(n)]
    cook = Cook(gh, n)
    min_synergy = cook.get_min_synergy()
    print(f"#{test} {min_synergy}")

import sys
from itertools import combinations, permutations

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]

    ingredients = list(combinations(range(N), N // 2))  # 음식 두 개가 재료를 반씩 나눠가지므로 N//2로 조합을 만들어줌

    ans = 20000

    for i in range(len(ingredients) // 2):
        ingredients_1 = ingredients[i]  # 음식 1의 재료 조합
        ingredients_2 = ingredients[len(ingredients) - i - 1]  # 음식 1에 들어가지 않은 음식 2의 재료 조합

        food_1 = 0
        food_2 = 0

        # 재료들에서 2개씩 뽑아 순열 만들어서 해당 좌표 값을 각 음식에 더해줌
        permus_1 = list(permutations(ingredients_1, 2))
        permus_2 = list(permutations(ingredients_2, 2))

        for permu in permus_1:
            food_1 += data[permu[0]][permu[1]]

        for permu in permus_2:
            food_2 += data[permu[0]][permu[1]]

        temp = abs(food_1 - food_2)

        if temp < ans:
            ans = temp

    print("#{} {}".format(tc, ans))

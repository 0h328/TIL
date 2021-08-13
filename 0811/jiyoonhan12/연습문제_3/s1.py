# nums = [1, 2, 3, 4]
# bits = [0, 0, 0, 0]

ingredients = ['egg', 'cheese', 'rice']

N = len(ingredients)

for i in range(1, 1 << N):
    for j in range(N):
        if i & (1 << j):
            print(ingredients[j], end=' ')
    print()
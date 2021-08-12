nums = [1, 2, 3, 4]
bits = [0, 0, 0, 0]

for i in range(2):
    bits[0] = i
    for j in range(2):
        bits[1] = j
        for k in range(2):
            bits[2] = k
            for l in range(2):
                bits[3] = l
                # print(*bits)
                # print(nums)
                for z in range(4):
                    if bits[z] == 1:
                        print(nums[z], end=' ')
                print()

ingredients = ['egg', 'cheeze', 'rice']

N = len(ingredients)

for i in range(1, 1 << N):
    for j in range(N):
        if i & (1 << j):
        # print(1 << j)
        # 1 2 4
        # -> i는 1 ~ 7
            print(ingredients[j], end=' ')
    print()

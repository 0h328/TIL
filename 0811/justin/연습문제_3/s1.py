#1. 부분집합 구하기 - for
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
                print(*bits)
                # print(nums)
                for z in range(4):
                    if bits[z] == 1:
                        print(nums[z], end=' ')
                print()

#2. 부분집합 구하기 - bitwise operator
ingredients = ['egg', 'cheeze', 'rice']
N = len(ingredients)
for i in range(1, 1 << N):
    for j in range(N):
        # print(i & (1 << j))
        # if i & (1 << j):
        # print(1 << j)
        # 1 2 4
        # -> i는 1 ~ 7
        print(ingredients[j], end=' ')

# 추가 자료는 아래 링크 참고
# https://www.notion.so/hphk/4b4ad14757ee49308e188e9f359ffe84
import sys
sys.stdin = open('input.txt')

# case 1
change = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
cnt = 0
for coin in coins:
    while change >= coin:
        cnt += 1
        change -= coin

print(cnt)

# case 2
# change = 1000 - int(input())
# coins = [500, 100, 50, 10, 5, 1]
# cnt = 0
# for coin in coins:
#     cnt += change // coin
#     change %= coin
# 
# print(cnt)
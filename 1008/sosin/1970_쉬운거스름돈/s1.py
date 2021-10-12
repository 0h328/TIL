import sys
sys.stdin = open('input.txt')

money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for T in range(int(input())):
    result = []
    rest_money = int(input())
    
    for m in money_list:
        result.append(rest_money//m)
        rest_money%=m

    print('#{}'.format((T+1)))
    print(*result)

# #1
# 0 3 0 2 1 3 1 0
# #2
# 0 0 0 0 0 1 1 1
# #3
# 11 1 0 2 0 4 0 1
# #4
# 2 4 1 3 1 4 1 0
# #5
# 20 0 0 0 0 0 0 0
# #6
# 0 1 1 1 1 0 0 4
# #7
# 0 0 0 0 0 0 0 3
# #8
# 0 0 0 0 0 0 0 1
# #9
# 1 1 1 1 1 1 1 1
# #10
# 19 4 1 4 1 4 1 4
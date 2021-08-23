import sys
sys.stdin = open('input.txt')

T = int(input())

# def find_answer(N):
#     ans = 0
#     if (N//10) == 1:
#         return 1
#     for n in range(2, (N//10)+1):
#         if n % 2:
#             ans = 2 * find_answer((n - 1) * 10) - 1
#         else:
#             ans = 2 * find_answer((n - 1) * 10) + 1
#     return ans

def find_answer2(N):
    ans = 0
    global memo
    if (N//10) >= 1 and len(memo) <= (N//10):
        if (N//10) % 2:
            memo.append(2 * find_answer2((((N//10)-1)*10)) - 1)
        else:
            memo.append(2 * find_answer2((((N//10)-1)*10)) + 1)

    return memo[N//10]



for test_case in range(1, T+1):
    N = int(input())
    memo = [1]
    # print('#{} {}'.format(test_case, find_answer(N)))
    print('#{} {}'.format(test_case, find_answer2(N)))


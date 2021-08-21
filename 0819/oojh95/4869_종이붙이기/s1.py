import sys
sys.stdin = open('input.txt')
def factorial(num):
    table[0] = 1

    for i in range(1, num+1):
        table[i] = i* table[i-1]
    return table[num]
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    result = 1
    table = [0] * (N//10)
    for j in range(1, N // 20 + 1):
        k = (N - j * 20) // 10
        result += (factorial(j + k)//(factorial(j)*factorial(k))) * (2**j)

    print('#{} {}'.format(test_case, result))
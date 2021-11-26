import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    num1 = list(map(int, input().split()))
    num2 = list(map(int, input().split()))

    n = len(num2)
    m = n // 2
    result = 0
    for i in range(len(num1)):
        while m > 0:
            if num1[i] > num2[m]:
                num = num2[m:]
            else:
                num = num2[:m]
            if num1[i] in num2:
                result += 1
                break
            m = m // 2






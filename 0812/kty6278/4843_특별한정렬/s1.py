import sys
import math
# from collections import deque
sys.stdin = open('input.txt')

# help.............................................................me
T = int(input())
for t in range(T):
    num = int(input())
    numbers = list(map(int, input().split()))

    result = []
    numbers.sort()

    for i in range(len(numbers)//2):
        result.append(numbers[len(numbers)-1-i])
        result.append(numbers[i])
    # print(result)
    """
    if num % 2 == 0:
        for i in range(num // 2):
            word = numbers.pop()
            result.append(word)
            result.append(numbers[i])
    else:
        for j in range(num // 2):
            word = numbers.pop()
            result.append(word)
            result.append(numbers[j])
        result.append(numbers[round(num//2)])
    """
    """
    result = ' '.join(map(str, result))
    print("#{} {}".format(t + 1, result))
    """

    """    
    print('#{}'.format(t + 1), end = ' ')
    for k in result:
       print('{}'.format(k), end = ' ')
    print()
    """
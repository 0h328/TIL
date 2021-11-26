import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(T):
    N = int(input())
    result = []
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        if 2**a * 3**b * 5**c * 7**d * 11**e == N:
                            result = [a, b, c, d, e]

    print("#{} ".format(num+1), end='')
    for i in result:
        print("{}".format(i), end=' ')
    print()
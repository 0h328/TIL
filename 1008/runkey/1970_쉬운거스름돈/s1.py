import sys
sys.stdin = open('input.txt')

tc = int(input())
for t in range(1, tc + 1):
    print("#{}".format(t))
    N = int(input())
    money = 100000
    for i in range(8):
        if i % 2:
            money //= 5
        else:
            money //= 2
        print(N // money, end=" ")
        N %= money
    print()


    # result.append(N // 50000)
    # N %= 50000
    # result.append(N // 10000)
    # N %= 10000
    # result.append(N // 5000)
    # N %= 5000
    # result.append(N // 1000)
    # N %= 1000
    # result.append(N // 500)
    # N %= 500
    # result.append(N // 100)
    # N %= 100
    # result.append(N // 50)
    # N %= 50
    # result.append(N // 10)
    #
    # for r in result:
    #     print(r, end=" ")
    # print()



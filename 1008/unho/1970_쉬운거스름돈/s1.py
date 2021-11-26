testCase = int(input())

for i in range(1, testCase+1):
    money = int(input())


    print('#{i}', end=' ')
    for i in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
        tmp = money//i
        money %= i
        print(tmp, end=' ')
    print()
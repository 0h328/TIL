testCase = int(input())

for i in range(1, testCase+1):
    money = int(input())
    
    first = money//50000
    money %= 50000

    second = money//10000
    money %= 10000

    third = money//5000
    money %= 5000

    fourth = money//1000
    money %= 1000

    fifth = money//500
    money %= 500

    sixth = money//100
    money %= 100

    seventh = money//50
    money %= 50

    eighth = money//10
    money %= 10

    print(f'#{i}\n{first} {second} {third} {fourth} {fifth} {sixth} {seventh} {eighth}')
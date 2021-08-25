import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    password = list(map(int, input().split()))
    result =''

    while password[-1] > 0:
        for i in range(1, 6):
            if password[-1] <= 0:
                break
            password.append(password.pop(0) - i)

    if password[-1] < 0:
        password[-1] = 0

    for j in password:
        result += str(j)

    print('#{} {}'.format(tc, ' '.join(result)))

'''
#1      6 2 2 9 4 1 3 0 
#2      9 7 9 5 4 3 8 0 
#3      8 7 1 6 4 3 5 0 
#4      7 5 8 4 8 1 3 0 
#5      3 8 7 4 4 7 4 0 
#6      6 7 5 9 6 8 5 0 
#7      7 6 8 3 2 5 6 0 
#8      9 2 1 7 3 6 3 0 
#9      4 7 8 1 2 8 4 0 
#10     6 8 9 5 8 5 2 0 
'''
import sys
sys.stdin = open('input.txt')

num = int(input())
divide = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for i in range(num):
    cnt = []
    money = int(input())
    for j in divide:
        cnt.append(money // j)
        money = money - (j * (money // j))

    print('#{0} \n{1}'.format(i + 1, ' '.join(map(str, cnt))))
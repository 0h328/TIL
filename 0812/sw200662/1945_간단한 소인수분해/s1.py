import sys
sys.stdin = open('input.txt')

T = int(input())

list1 = [2,3,5,7,11]

for i in range(T):
    Nums = int(input())
    cnt_ans = []
    print('#{}'.format(i + 1), end=' ')
    for k in list1:
        cnt = 0
        while Nums % k ==0:
            Nums = Nums//k
            cnt +=1
        print(cnt, end=' ')
    print()
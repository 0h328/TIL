import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    A,B = input().split()
    Test_case = list(map(str, input().split()))
    Num_case = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    print(A)
    for Nums in Num_case:
        cnt = 0
        for Test in Test_case:
            if Test == Nums:
                cnt +=1
        for a in range(cnt):
            print(Nums, end=' ')
        if Nums == 'NIN':
            print()




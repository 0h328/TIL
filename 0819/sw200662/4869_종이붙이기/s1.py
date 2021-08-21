import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    Nums = int(input())
    Nums = Nums//10
    list_Nums = [0] * Nums
    for k in range(Nums):
        if k == 0:
            list_Nums[0] = 1
        elif k == 1:
            list_Nums[1] = 3
        else:
            list_Nums[k] = list_Nums[k-1] + list_Nums[k-2] * 2
    print('#{} {}'.format(i+1,list_Nums[Nums-1]))


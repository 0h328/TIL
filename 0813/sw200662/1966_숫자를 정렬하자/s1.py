import sys
sys.stdin = open('input.txt')

def Bubble(Nums):
    for i in range(len(Nums)-1,0,-1):
        for k in range(i):
            if Nums[k] >= Nums[k+1]:
                Nums[k],Nums[k+1] = Nums[k+1],Nums[k]
    return(Nums)

def Counting(Nums):
    A = max(Nums)
    Counting_list = [0] * (A+1)
    ans = [0] * len(Nums)

    for i in Nums:
        Counting_list[i] += 1
    for k in range(A):
        Counting_list[k+1] += Counting_list[k]

    for z in Nums:
        ans[Counting_list[z]-1] = z
        Counting_list[z] -= 1
    return ans

def Selection(Nums):
    for i in range(len(Nums)):
        min_nums = Nums[i]
        cnt = i
        for k in range(i+1,len(Nums)):
            if min_nums > Nums[k]:
                min_nums = Nums[k]
                cnt = k
        if min_nums != Nums[i]:
            Nums[i], Nums[cnt] = Nums[cnt], Nums[i]

T = int(input())

for i in range(T):
    N = int(input())
    Nums = list(map(int,input().split()))
    # ans = Bubble(Nums)
    # print('#{}'.format(i+1),end=' ')
    # for k in ans:
    #     print(k,end=' ')
    # print()
    #Counting(Nums)
    #Selection(Nums)





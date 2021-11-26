import sys
sys.stdin = open('input.txt')

nums = list(map(int,input().split()))

def Bubble(num):
    for i in range(len(num)-1,0,-1):
        for k in range(i):
            if num[k] > num[k+1]:
                num[k],num[k+1] = num[k+1],num[k]

    return(num)

result = Bubble(nums)
print(result)


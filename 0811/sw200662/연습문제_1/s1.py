import sys
sys.stdin = open('input.txt')

T = int(input())
numbers = []
for i in range(T):
    nums = list(map(int,input().split()))
    numbers.append(nums)

def hang(a):
    ans = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            ans.append(a[i][j])
    return(ans)

def yeol(a):
    ans = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            ans.append(a[j][i])
    return(ans)

def zigzag(a):
    ans = []
    for i in range(len(a)):
        if i % 2 == 0:
            for k in range(len(a[i])):
                ans.append(a[i][k])

        else:
            for k in range(len(a[i])):
                for_inx = len(a[i])-1-k
                ans.append(a[i][for_inx])
    return ans

def junzhi(a):
    ans = []
    for i in range(len(a[0])):
        temp_list=[]
        for k in range(len(a)):
            temp_list.append(a[k][i])
            ans.append(temp_list)

    return ans


print(hang(numbers))
print(yeol(numbers))
print(zigzag(numbers))
print(junzhi(numbers))


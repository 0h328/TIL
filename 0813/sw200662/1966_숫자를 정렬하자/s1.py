import sys
sys.stdin = open('input.txt')

def Bubble(Nums):
    for i in range(len(Nums) - 1, 0, -1):
        for k in range(i):
            if Nums[k] >= Nums[k + 1]:
                Nums[k], Nums[k + 1] = Nums[k + 1], Nums[k]
    return Nums

def Counting(Nums):
    A = max(Nums) # 최고 숫자를 우선 판별하고
    Counting_list = [0] * (A + 1) # 그숫자 + 1만큼의 list가 필요하니 생성해준 다음
    ans = [0] * len(Nums) # 답에는 숫자 만큼만 필요하니 len(nums)를통하여 리스트 생성

    for i in Nums: # 카운팅 리스트에 하나하나 더해주고
        Counting_list[i] += 1
    for k in range(A): # 카운팅 리스트에 각각을 누적(뒤로 누적)
        Counting_list[k + 1] += Counting_list[k]
    for z in Nums: # 자리를 찾아가며 하나씩 입력
        ans[Counting_list[z] - 1] = z
        Counting_list[z] -= 1
    return ans

def Selection(Nums):
    for i in range(len(Nums)-1):
        min_nums = Nums[i] # 최소숫자를 음수일수 있으니 최소값을 하나 넣고
        cnt = i
        for k in range(i + 1, len(Nums)): # 앞에서부터 하나씩 해가면서 맨 앞으로 정렬할것이므로
            if min_nums > Nums[k]:
                min_nums = Nums[k]
                cnt = k
        if min_nums != Nums[i]:
            Nums[i], Nums[cnt] = Nums[cnt], Nums[i]
    return(Nums)

T = int(input())

for i in range(T):
    N = int(input())
    Nums = list(map(int, input().split()))
    # ans = Bubble(Nums)
    # print('#{}'.format(i+1),end=' ')
    # for k in ans:
    #     print(k,end=' ')
    # print()
    # Counting(Nums)
    # Selection(Nums)

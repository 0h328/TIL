def dfs(cnt,num):
    global max_money
    if cnt == N:
        money = 0
        for i in range(len(num)):
            money += num[i] * (10 ** (len(num) - 1 - i))
        if money > max_money:
            max_money = money
        return
    for i in range(length):
        for j in range(i+1,length):
            num[i],num[j] = num[j], num[i]
            str_num = ""
            for n in num:
                str_num += str(n)
            if visited.get((str_num,cnt+1),1):
                visited[(str_num,cnt+1)] = 0
                dfs(cnt+1,num)
            num[i],num[j] = num[j], num[i]

T = int(input())
for tc in range(1,T+1):
    tmp, N = input().split()
    num = []
    for n in tmp:
        num.append(int(n))
    N = int(N)
    length = len(num)
    max_money = 0
    visited = {}
    dfs(0,num)
    print("#{} {}".format(tc, max_money))

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = [0 for _ in range(N+1)]
    temp = list(map(int, input().split()))
    papers = [[] for _ in range(N+1)]

    for i in range(N+1):
        papers[i].append(i)

    for i in range(len(temp)//2):
        papers[temp[2*i]].append(temp[2*i+1])
        papers[temp[2*i+1]].append(temp[2*i])
    print(papers)
    for num in papers:
        num.sort()

    # print(papers)
    ans = []
    for num in papers:
        if num not in ans:
            ans.append(num)
    # for num in ans:
    #     if
    print(ans)
    ans2 = []
    for num in papers:
        ans2.append(set(num))
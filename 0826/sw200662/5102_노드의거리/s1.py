import sys
sys.stdin = open('input.txt')

T = int(input())

def find(a,b):
    global ans
    visit[a] = 1
    for w in list_node[a]:
        if not visit[w]:
            if w == G:
                temp_ans = b + 1
                if temp_ans < ans:
                    ans = temp_ans
            find(w,b+1)


for i in range(T):
    V,E = map(int,input().split())
    list_node = [[] for _ in range(V + 1)]
    visit = [0] * (V + 1)
    ans = 5555
    for _ in range(E):
        A,B = map(int,input().split())
        list_node[A].append(B)
        list_node[B].append(A)
    print(list_node)
    S,G = map(int,input().split())
    find(S,0)
    if ans == 5555:
        ans = 0
    print('#{} {}'.format(i+1,ans))
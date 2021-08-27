import sys
sys.stdin = open('input.txt')

T = int(input())

def find(x):
    global cnt
    que = []
    que.append(list_node[x])
    visit[x] = 1

    while que:
        temp_list = []
        z = que.pop(0)
        cnt += 1
        for k in z:
            if visit[k] == 0:
                visit[k] = cnt
                temp_list += list_node[k]
            if k == G:
                return visit[k]
        que.append(temp_list)



for i in range(T):
    V,E = map(int,input().split())
    list_node = [[] for _ in range(V + 1)]
    visit = [0] * (V + 1)
    cnt = 0
    for _ in range(E):
        A,B = map(int,input().split())
        list_node[A].append(B)
        list_node[B].append(A)
    S,G = map(int,input().split())
    print('#{} {}'.format(i+1,find(S)))

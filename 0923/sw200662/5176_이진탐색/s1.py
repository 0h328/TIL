def find_num(node):
    global cnt

    if node <= N:
        find_num(node*2)

        tree[node] = cnt
        cnt += 1

        find_num(node*2+1)



T = int(input())

for i in range(T):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    find_num(1)
    print('#{} {} {}'.format(i+1,tree[1],tree[N//2]))
import sys
sys.stdin = open('input.txt')

def sort(k):
    while k != 1:
        if tree[k] < tree[k//2]:
            tree[k], tree[k//2] = tree[k//2], tree[k]
        k = k//2


def plus(b):
    global cnt
    cnt += 1
    tree.append(b)
    sort(cnt)

def sum_ans(c):
    ans = 0
    while c != 1:
        ans += tree[c//2]
        c = c//2
    return ans
T = int(input())
for tc in range(T):
    N = int(input())
    tree = [0]
    num_list = list(map(int,input().split()))
    cnt = 0
    for z in num_list:
        plus(z)
    print('#{} {}'.format((tc+1),sum_ans(N)))

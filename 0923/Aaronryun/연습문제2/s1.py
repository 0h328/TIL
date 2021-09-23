

def pre(node):
    global cnt
    if node !=0:
        cnt+=1
        print('{}'.format(node),end=' ')
        pre(tree[node][0])
        pre(tree[node][1])

def in_order(node):
    global cnt
    if node !=0:
        in_order(tree[node][0])
        print('{}'.format(node),end=' ')
        in_order(tree[node][1])

def post(node):
    global cnt
    if node !=0:
        post(tree[node][0])
        post(tree[node][1])
        print('{}'.format(node),end=' ')

import sys
sys.stdin = open('input.txt')
V = int(input())
E = V-1

tree = [[0 for _ in range(3)] for _ in range(V+1)]
temp = list(map(int,input().split()))
cnt = 0
for i in range(E):
    parent,child = temp[i*2],temp[i*2+1]
    if not tree[parent][0]:
        tree[parent][0] = child
    else:
        tree[parent][1]=child
    tree[child][2]=parent

print('pre : ',end=' ')
pre(1)
print()
print(cnt)
print(cnt-1)
print()

print('in : ',end = ' ')
in_order(1)
print()

print('post : ',end=' ' )
post(1)
print()
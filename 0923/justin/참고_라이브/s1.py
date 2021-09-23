def pre_order(n):
    global cnt
    if n:                    # 자식이 있는 정점이면
        cnt += 1
        print(n)
        pre_order(left[n])   # n의 왼쪽 자식으로 이동
        pre_order(right[n])  # n의 오른쪽 자식으로 이동

def in_order(n):
    if n:                    # 자식이 있는 정점이면
        pre_order(left[n])   # n의 왼쪽 자식으로 이동
        print(n)
        pre_order(right[n])  # n의 오른쪽 자식으로 이동

def post_order(n):
    if n:                    # 자식이 있는 정점이면
        pre_order(left[n])   # n의 왼쪽 자식으로 이동
        pre_order(right[n])  # n의 오른쪽 자식으로 이동
        print(n)

V = int(input())
E = V - 1
edge = list(map(int, input().split()))
left = [0] * (V+1)              # 부모를 인덱스로 자식 번호 저장
right = [0] * (V+1)             # 부모를 인덱스로 자식 번호 저장
par = [0] * (V+1)               # 자식을 인덱스로 부모 번호 저장

for i in range(E):
    parent, child = edge[i*2], edge[i*2+1]
    if left[parent] == 0:       # parent의 왼쪽 자식이 없으면
        left[parent] = child    # 왼쪽 자식으로 저장
    else:                       # 왼쪽 자식이 있으면
        right[parent] = child   # 오른쪽 자식으로 저장

    par[child] = parent         # (1) 조상을 찾는데 사용 & (2) root를 찾는데 사용

# 조상 찾기
c = 6
while par[c]:
    print(par[c]) # 부모 번호 찍고
    c = par[c]    # 부모의 부모 찾기

# 부모가 없으면 root
root = 1
while par[root]: # root로 추정한 정점이 부모가 있으면
    root += 1
print(root)

# cnt = 0
# pre_order(1)
# print(cnt)      # 1을 루트로하는 서브트리의 정점 개수
# print(cnt-1)    # 3의 자손 수
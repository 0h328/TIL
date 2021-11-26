import sys
sys.stdin=open('input.txt')
def make_set(x):
    p[x] = x                     # 노드 x의 부모 저장

def find_set(x):
    if p[x] != x:                # x가 루트가 아닌 경우
        p[x] = find_set(p[x])    # 다시 루트 찾아서 재귀 호출
    return p[x]                  # x의 대표값 반환

def union(x, y):
    p[find_set(y)] = find_set(x) # y의 대표자를 x의 대표자로 변경

def kruskal():
    global ans
    edge_cnt = idx = 0

    while edge_cnt != V:
        x = data[idx][0]
        y = data[idx][1]

        if find_set(x) != find_set(y):      # 같은 부모를 공유하고 있지 않은 경우
            union(x, y)                      # 합친다
            edge_cnt += 1                    # 간선 갯수 증가
            ans += data[idx][2]            # 누적치 증가
        idx += 1                            # 다음 간선 선택

for test in range(1,1+int(input())):
    V,E = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(E)]
    p = [0]*(V+1)
    ans = 0
    data = sorted(data,key=lambda x:x[2])

    for i in range(V+1):
        make_set(i)

    kruskal()
    print('#{} {}'.format(test,ans))
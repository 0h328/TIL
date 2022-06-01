import sys
sys.stdin = open('input.txt')

tree = {}
cnt = 0     # 모든 이름 개수를 세기 위한 변수
while True:
    name = sys.stdin.readline().rstrip()
    if name == '':          # 종료 조건
        break

    if name not in tree:    # 이름이 tree에 없으면
        tree[name] = 1      # 이름: 1 형식으로 dict에 추가
    else:                   # 이름이 tree에 있으면
        tree[name] += 1     # value에 개수 추가

    cnt += 1

tree_info = list(tree.keys())   # 이름을 list에 저장
tree_info.sort()                # 정렬

for t in tree_info:
    print(t, '%.4f' %(tree[t]/cnt*100))
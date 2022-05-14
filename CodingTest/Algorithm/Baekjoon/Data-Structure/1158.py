import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
q = [i+1 for i in range(N)]

ans = []
no = 0  #

for _ in range(N):
    no += K-1   # [1,2,3,4,5,6,7] -> [1,2,4,5,6,7] -> [1,2,4,5,7] 줄어드므로 K-1
    if no >= len(q):        # 번호가 큐의 길이보다 크면
        no = no % len(q)    # 길이만큼 나눠서 인덱스 처리

    ans.append(str(q.pop(no)))

print('<', ', '.join(ans), '>', sep='')


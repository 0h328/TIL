import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

# set 자료형은 교집합, 합집합, 차집합 구할때 사용됨.
n_h = set()
for i in range(N):
    n_h.add(sys.stdin.readline().strip())

n_s = set()
for i in range(M):
    n_s.add(sys.stdin.readline().strip())

res = sorted(list(n_h & n_s))   # &로 n_h와 n_s의 교집합을 찾아줌
# res = sorted(list(n_h.intersection(n_s)))
# n_h | n_s 혹은 n_h.union(n_s)는 합집합
# n_h - n_s 혹은 n_h.difference(n_s)는 차집합

print(len(res))

for i in res:
    print(i)

# n_heard = [input().strip() for _ in range(N)]
# n_seen = [input().strip() for _ in range(M)]
#
# intersection = sorted(list(set(n_heard) & set(n_seen)))
#
# print(len(intersection))
# for i in intersection:
#     print(i)
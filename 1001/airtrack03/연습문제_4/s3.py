"""
연습문제 4. 순열

4-3) 5개의 숫자 중 3자리의 순열 생성하기
[1, 2, 3, 4, 5]에서 3자리의 순열을 재귀 함수를 활용하여 구현하시오.
"""

def perm(n, k, m): 		# n: 숫자를 결정 할 자리 인덱스, k: 순열의 길이, m: 주어진 숫자의 개수
    if k == m:
        print(*p)
        return
    else:
        for i in range(N):
            if not visited[i]:
                p[k] = nums[i]
                visited[i] = 1
                perm(n, k+1, m)
                visited[i] = 0

nums = [1, 2, 3, 4, 5]
N, M = 5, 3
p = [0] * M
visited = [0] * N
perm(N, 0, M)

"""
1 2 3 
1 2 4 
1 2 5 
1 3 2 
1 3 4 
1 3 5 
1 4 3 
1 4 2 
1 4 5 
1 5 3 
1 5 4 
1 5 2 
2 1 3 
2 1 4 
2 1 5 
2 3 1 
2 3 4 
... 생략
"""
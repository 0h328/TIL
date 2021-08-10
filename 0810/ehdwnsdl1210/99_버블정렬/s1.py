import sys
sys.stdin = open('input.txt')

N = list(map(int, input().split()))

for i in range(len(N)-1, 0, -1):        # 우측 끝에서부터 처음 까지 훑음
    for j in range(i):                  # 인덱스 활용을 위해 이중 for문
        if N[j] > N[j+1]:               # 왼쪽 > 오른쪽
            N[j], N[j+1] = N[j+1], N[j] # 자리 맡바꿈 (우측 끝쪽에 큰수가 오도록)
print(N)

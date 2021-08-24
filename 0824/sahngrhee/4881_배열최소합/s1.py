'''
순열을 이용해서 어떻게든 해볼려고 했지만 시간초과
'''

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

def permutation(idx):
    global pair
    if idx == N:  # 자리를 다 잡았으면 출력하세요, 모든 자리를 다 결정했나요?
        pair += sel
        # pair += [sel]
        # pair.append(sel)
        return
    for i in range(N):
        if check[i] == 0:  # 해당 원소를 아직 사용하지 않았다면
            sel[idx] = arr[i]  # 원소가 있는 자리에 arr에 i번째 요소를 넣자
            check[i] = 1  # 해당 원소를 사용했다고 체크해주자
            permutation(idx + 1)  # 다음 자리를 확인하러 가자!
            check[i] = 0  # 다음 반복을 위해 원상복구 시켜주자

import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]

    arr = [n for n in range(N)]
    sel = [0] * N
    check = [0] * N
    pair = []
    permutation(0)
    pair_list = []
    for k in range(1, factorial(N)+1):
        pair_list.append(pair[(k-1)*N:k*N])

    ans = 90
    for pair in pair_list:
        total = 0
        for i in range(N):
            total += numbers[i][pair[i]]
        if ans > total:
            ans = total

    print('#{} {}'.format(test_case, ans))


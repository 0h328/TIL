import sys
sys.stdin = open('input.txt')

C = [0] * 10

def counting(A,B,k):
    for i in range(len(B)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= -1

num = int(input())
for _ in range(num):
    cnt_list = list(map(int,input().split()))
    print(counting(cnt_list))
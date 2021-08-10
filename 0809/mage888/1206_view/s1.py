import sys
sys.stdin = open('input.txt')

for no in range(1, 11):
    N = int(input())
    A = list(map(int, input().split()))

    total = 0
    for i in range(2, len(A)-2):
        if A[i] > A[i-1] and A[i] > A[i-2] and A[i] > A[i+1] and A[i] > A[i+2]:

            B_list = [A[i-2], A[i-1], A[i+1], A[i+2]]
            max_value = B_list[0]
            for k in B_list:
                if max_value < k:
                    max_value = k
            total += A[i]-max_value

    print("#{} {}".format(no, total))
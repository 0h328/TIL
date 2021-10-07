#1-1. 조합에 대한 기본적인 방법

# 3C2
# arr = ['A', 'B', 'C']
# N = len(arr)
#
# # i: N-1은 남겨놔야 하기 때문에 N-2까지 진행
# for i in range(N-1):
#     # j: i 다음부터 N-1까지 본다.
#     for j in range(i+1, N):
#         print(arr[i], arr[j])


# 5C3
arr = ['A', 'B', 'C', 'D', 'E']
N = len(arr)
for i in range(N-2):                        # i: N-3은 남겨놔야 하기 때문에 N-2까지 진행
    for j in range(i+1, N-1):               # j: i 다음부터 N-2까지
        for k in range(j+1, N):
            print(arr[i], arr[j], arr[k])
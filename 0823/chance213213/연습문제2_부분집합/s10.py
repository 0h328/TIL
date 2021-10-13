arr = [1, 2, 3]
N = len(arr)
sel = [0] * N
#
# def powerset(idx):
#     for i in range(2**N):
#         for j in range(N):
#             if i & (1 << j):
#                 sel[j] = 1
#             else:
#                 sel[j] = 0
#
#
# powerset(0)

def powerset(idx):
    if idx == N:
        print(sel)
        for i in range(N):
            if arr[i]*sel[i]:
                print(arr[i]*sel[i], end=' ')
        print()
    else:
        sel[idx] = 1
        powerset(idx+1)
        sel[idx] = 0
        powerset(idx+1)

powerset(0)
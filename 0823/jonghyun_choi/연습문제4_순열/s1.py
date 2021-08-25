arr = [1, 2, 3]
N = len(arr)
sel = [0] * N
check = [0] * N

def permutation(idx):
    if idx == N:
        print(sel)
        return

    for i in range(N):
        if check[i] == 0:
            sel[idx] = arr[i]
            check[i] = 1
            permutation(idx + 1)
            check[i] = 0




permutation(0)
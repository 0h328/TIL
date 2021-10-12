arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N
results = []


def powerset(idx):
    if idx == N:
        print(sel)
    else:
        sel[idx] = 1
        powerset(idx + 1)
        sel[idx]
        powerset(idx + 1)

powerset(0)

import sys
sys.stdin = open('input.txt')

def merge_sort(l):
    if len(l) == 1:
        return l
    else:
        return merge(merge_sort(l[:len(l)//2]), merge_sort(l[len(l)//2:]))

def merge(l1, l2):
    global res1
    merged = []
    idx1 = 0
    idx2 = 0
    while idx1 < len(l1) and idx2 < len(l2):
        if l1[idx1] <= l2[idx2]:
            merged.append(l1[idx1])
            idx1 += 1
        else:
            merged.append(l2[idx2])
            idx2 += 1

    if idx2 == len(l2):
        res1 += 1
        merged += l1[idx1:]
    else:
        merged += l2[idx2:]
    return merged

t = int(input())
for idx in range(1, t+1):
    n = int(input())
    l = list(map(int, input().split()))
    res1 = 0
    l = merge_sort(l)

    print('#{} {} {}'.format(idx, l[n//2], res1))
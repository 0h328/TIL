import sys
sys.stdin = open('input.txt')

def check(lst):
    for i in range(len(lst)//2):
        if lst[i] != lst[-i-1]:
            return False
    return True

for _ in range(1, 11):
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    arr2 = list(zip(*arr))

    max_pal = 1

    for l in range(100, 1, -1):
        if max_pal > l:
            break
        for idx in range(100-l+1):
            if max_pal == l:
                break
            for lst, lst2 in zip(arr, arr2):
                if check(lst[idx:idx+l]) or check(lst2[idx:idx+l]):
                    max_pal = l
                    break
    print('#{} {}'.format(T, max_pal))


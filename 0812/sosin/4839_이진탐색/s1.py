import sys
sys.stdin = open('input2.txt')

# ????????? 이해불가

def binary_search(s, e, target, count):
    mid = (s+e)//2
    if mid == target:
        return count
    elif mid > target:
        return binary_search(s, mid-1, target, count+1)
    else:
        return binary_search(mid+1, e, target, count+1)

for T in range(int(input())):
    p, a, b = map(int,input().split())
    a_count = binary_search(1, p, a, 1)
    b_count = binary_search(1, p, b, 1)

    print('#{}'.format((T+1)), end=' ')

    if a_count == b_count:
        print(0)
    else:
        print('A' if a_count<b_count else 'B')

#1 A
#2 0
#3 A
import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    P,A,B = map(int,input().split())
    start = 1
    end = P
    cnt1 = 0
    cnt2 = 0
    while start <= end:
        middle = (start + end) // 2
        cnt1 += 1
        if middle == A:
            break
        elif middle > A:
            end = middle
        else:
            start = middle
    if start > end: # < 만약 범위를 벗어날경우 실패했으므로 0으로 가정정
       cnt1 = 0

    start = 1
    end = P
    while start <= end:
        cnt2 += 1
        middle = (start + end) // 2
        if middle == B:
            break
        elif middle > B:
            end = middle
        else:
            start = middle
    if start > end:
        cnt2 = 0

    if cnt1 < cnt2:
        print('#{} {}'.format(i+1,'A'))
    elif cnt1 > cnt2:
        print('#{} {}'.format(i+1,'B'))
    else:
        print('#{} {}'.format(i+1,'0'))
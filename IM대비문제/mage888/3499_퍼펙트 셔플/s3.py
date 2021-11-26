import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = input().split()

    mid = len(data)//2
    left = data[:mid]
    right = data[mid:]

    ans = []

    if len(data) % 2 == 0:
        for i in range(len(data)//2):
            ans.append(left[i])
            ans.append(right[i])

    else:
        left = data[:mid+1]
        right = data[mid+1:]
        for i in range(len(data)//2):
            ans.append(left[i])
            ans.append(right[i])
        ans.append(left[len(left)-1])

    print('#{} {}'.format(tc, ' '.join(ans)))

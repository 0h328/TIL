import sys
sys.stdin = open('input.txt')


def iswin(a):
    for i in range(len(a)):
        if a[i] > 2: return True

        if i > 1:
            if a[i-2] and a[i-1] and a[i]: return True
    return False


ans = []
T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    p1, p2 = [0] * 10, [0] * 10
    for i in range(0, len(arr), 2):
        p1[arr[i]] += 1
        p2[arr[i+1]] += 1

        if iswin(p1):
            ans.append('#{0} {1}'.format(tc, 1))
            break
        elif iswin(p2):
            ans.append('#{0} {1}'.format(tc, 2))
            break
    else:
        ans.append('#{0} {1}'.format(tc, 0))

print(*ans, sep='\n')

import sys
sys.stdin = open('input.txt')

def find_palindrome(l, m):
    for sub in [*l, *list(zip(*l))]:
        for i in range(n-m+1):
            inter = m - 1
            idx = i
            while inter > 1 and sub[idx] == sub[idx + inter]:
                inter -= 2
                idx += 1
            if inter < 2:
                return sub[i:i+m]

t = int(input())

for num in range(1, t+1):
    n, m = map(int, input().split())
    l = [list(input()) for _ in range(n)]
    print('#{} {}'.format(num, ''.join(find_palindrome(l, m))))

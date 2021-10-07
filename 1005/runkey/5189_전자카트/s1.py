import sys
sys.stdin = open('input.txt')

tc = int(input())

def p(a):
    length = len(a)
    if length == 1:
        return [a]
    else:
        result = []
        for i in a:
            b = a.copy()
            b.remove(i)
            b.sort()
            for j in p(b):
                j.insert(0, i)
                if j not in result:
                    result.append(j)
        return result

for t in range(1, tc + 1):
    result = []
    N = int(input())
    a = [x for x in range(1, N + 1)]
    c = p(a)
    x = [list(map(int, input().split())) for _ in range(N)]
    for i in c:
        temp = 0
        for idx in range(1, len(i)):
            temp += x[i[idx - 1] - 1][i[idx] - 1]
        temp += x[i[len(i) - 1] - 1][i[0] - 1]
        result.append(temp)
    print("#{} {}".format(t, min(result)))
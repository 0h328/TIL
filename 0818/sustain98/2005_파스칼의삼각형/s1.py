import sys
sys.stdin = open('input.txt')

t = int(input())
res = [[1]]
for idx in range(1, t+1):
    n = int(input())
    while len(res) < n:
        new_line = [1]
        for i in range(1, len(res)):
            new_line.append(res[-1][i-1] + res[-1][i])
        new_line.append(1)
        res.append(new_line)
    print('#{}'.format(idx))
    print('\n'.join(map(lambda x: ' '.join(map(str,x)), res)))



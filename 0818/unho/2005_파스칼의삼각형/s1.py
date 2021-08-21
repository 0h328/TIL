import sys
sys.stdin = open('input.txt')



test_case = int(input())

for tc in range(1, test_case+1):
    num = int(input())
    pascal = [[0, 1, 0]]

    for _ in range(num-1):
        tmp = [0]
        for idx in range(len(pascal[-1])-1):
            tmp.append(pascal[-1][idx] + pascal[-1][idx+1])
        tmp.append(0)
        pascal.append(tmp)


    print('#{}'.format(tc))
    for e in pascal:
        e.pop()
        e.pop(0)
        print(*e)
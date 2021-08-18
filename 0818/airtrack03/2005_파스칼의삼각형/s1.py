# 반복문 풀이

import sys

sys.stdin = open('input.txt')

T = int(input())

def triangle(num):
    ans = [[1]]

    # num == 1인 경우, 1만 return
    if num == 1:
        return ans
    # num != 1인 경우, 처음과 마지막은 1을 넣고, 그 외에는 바로 앞 리스트의 해당 인덱스와 그 앞 인덱스 값을 더해서 append
    for i in range(1, num):
        temp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(ans[i-1][j-1] + ans[i-1][j])
        ans.append(temp)

    return ans

for tc in range(1, T+1):
    N = int(input())

    ans = triangle(N)

    print('#{}'.format(tc))
    for line in ans:
        print(' '.join(map(str, line)))
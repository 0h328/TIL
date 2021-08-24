import sys
sys.stdin = open('input.txt')

def solve(num, my_list):
    adj_list = [[]for _ in range(100)]
    for i in range(0, num*2, 2):
        adj_list[my_list[i]].append(my_list[i + 1])

    visited = [0] * 100
    ans = 0

    stack = [0]

    while len(stack) > 0:
        curr = stack.pop()

        if curr == 99:
            ans = 1
            break
        # 방문하지 않았으면

        # 방문을 했으면 건너간다
        if visited[curr]:
            continue
        visited[curr] = 1

        for w in adj_list[curr]:
            if not visited[w]:
                stack.append(w)

    return ans

for i in range(10):
    testcase, num = map(int, input().split())
    my_list = list(map(int, input().split()))
    print('#{} {}'.format(testcase, solve(num, my_list)))
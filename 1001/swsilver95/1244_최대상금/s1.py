import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def dfs(cnt):
    global answer
    if cnt >= N:
        answer = max(answer, int(''.join(map(str, numbers))))
        return

    else:
        # 두 자리를 모두 바꾸는 과정
        for i in range(M - 1):
            for j in range(i + 1, M):
                # 두 자리를 바꿔서
                numbers[i], numbers[j] = numbers[j], numbers[i]
                # 숫자로 바꿔준다.
                num = int(''.join(map(str, numbers)))
                # 해당 숫자가 같은 교환 횟수에서 등장한적이 있다면 다시 할 필요 없음
                if (num, cnt) not in visited:
                    visited.add((num, cnt))
                    dfs(cnt + 1)
                # 바꾼 숫자 원상 복구
                numbers[i], numbers[j] = numbers[j], numbers[i]


for tc in range(1, T + 1):
    tmp, N = map(str, input().strip().split())
    N = int(N)
    M = len(tmp)
    numbers = list(map(int, tmp))
    visited = set()
    answer = 0
    dfs(0)
    print('#{} {}'.format(tc, answer))

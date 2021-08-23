import sys

sys.stdin = open('input.txt')

# 컨셉 : 최댓값이 등장한다? 그러면 쭉 빼고 새로운 최댓값이 나온다? 최댓값을 갱신하고 쭉빼고 하면 되는거였다....
# 처음 최댓값을 0으로 설정해서 최초인덱스를 최댓값으로 받고 순회하면서 새로운 최댓값이 나올때까지는 값에 더하고 최댓값이 나오면 갱신한다.
# 핵심은 최댓값이 등장하면 쭉빼줘야 하기 때문에 리버스가 필요하다 정방향으로 탐색하게 되면 최댓값이 갱신된뒤에 지나온 인덱스를 확인해야 하지만
# 거꾸로 뒤집어 놓으면 앞으로 갈 인덱스가 과거이기 떄문에... 최댓값이 아니라면 차이만 계산하면 된다

for test in range(1, 1 + int(input())):

    N = int(input())

    data = list(map(int, input().split()))

    max_data = 0
    answer = 0

    data.reverse()

    for i in data:
        if max_data < i:
            max_data = i
        else:
            answer += (max_data - i)

    print('#{} {}'.format(test, answer))


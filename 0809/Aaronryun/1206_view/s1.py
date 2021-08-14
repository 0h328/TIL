import sys

sys.stdin = open('input.txt')
for test in range(10):

    N = int(input())
    apart = list(map(int, input().split()))
    cnt = 0

    # 아파트를 기준으로 양 옆 아파트의 길이를 뺐을 때 값이 양수이면 조망권이 확보되는 층이 존재
    # 뺀 아파트 값이 가장 작은 것이 가장 큰 길이의 아파트와의 차이이므로
    for i in range(2, N - 2):
        if apart[i] - apart[i - 1] > 0 and apart[i] - apart[i - 2] > 0 and apart[i] - apart[i + 1] > 0 and apart[i] - \
                apart[i + 2] > 0:
            cnt += min(apart[i] - apart[i - 1], apart[i] - apart[i - 2], apart[i] - apart[i + 1],
                       apart[i] - apart[i + 2])

    print('#{} {}'.format(test + 1, cnt))

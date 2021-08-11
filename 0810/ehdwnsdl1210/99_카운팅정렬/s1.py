import sys
sys.stdin = open('input.txt')           # 기존 배열 N
                                        # count 줄 (숫자 센거 인덱스에 맞춰서) count
N = list(map(int, input().split()))     # 새로 정렬 된 배열 sorted_result
# 3 3 4 4 5 5 6 0 1 2 2 2
def counting_sorted(N):
    sorted_result = [0] * len(N)
    count = [0] * (max(N) + 1)      # 0부터 시작이라서

    for i in range(0, len(sorted_result)):
        count[N[i]] += 1            # 본 숫자를 인덱스로 순서줘서 count 올려주고

    for i in range(1, len(count)):
        count[i] += count[i - 1]    # 누적 / 밑에 해당하는거 없에면서 할거라

    for i in range(len(sorted_result) - 1, -1, -1):     # 거꾸로, 안정정렬
        sorted_result[count[N[i]] - 1] = N[i]
        count[N[i]] -= 1

    return sorted_result

print(counting_sorted(N))
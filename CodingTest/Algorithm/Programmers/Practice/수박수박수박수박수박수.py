# 수박수박수박수박수박수 Level 1
def solution(n):

    # 풀이1
    answer = ''
    a = '수박'
    for i in range(n):
        if i % 2:
            answer += a[1:]
        else:
            answer += a[:1]

    return answer

    # 풀이2
    # s = "수박" * n
    # return s[:n]


print(solution(3))
print(solution(4))

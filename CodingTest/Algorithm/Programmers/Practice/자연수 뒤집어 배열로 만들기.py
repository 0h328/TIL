# 자연수 뒤집어 배열로 만들기 Level 1

def solution(n):
    # answer = []
    #
    # while n > 1:
    #     answer.append(int(n % 10))
    #     n /= 10
    #
    # return answer

    return [int(str(n)[i-1]) for i in range(len(str(n)), 0, -1)]

    # return list(map(int, reversed(str(n))))

    # return [int(i) for i in str(n)][::-1]

print(solution(12345))
print(solution(13245))


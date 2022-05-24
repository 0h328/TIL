# 행렬의 덧셈 Level1
# import numpy as np

def solution(arr1, arr2):
    answer = []

    # 풀이1
    # for i in range(len(arr1)):
    #     answer.append([])
    #     for j in range(len(arr1[i])):
    #         answer[i].append(arr1[i][j] + arr2[i][j])

    # 풀이2
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]

    # 풀이3
    # A = np.array(arr1)
    # B = np.array(arr2)
    # answer = A+B
    # return answer.tolist()

    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
print(solution([[1],[2]], [[3],[4]]))
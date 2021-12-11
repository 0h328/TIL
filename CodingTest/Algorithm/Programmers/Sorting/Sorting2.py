def solution(array, commands):
    answer = []
    cut_array = []

    for i in range(len(commands)):
        cut_array.append(array[commands[i][0]-1:commands[i][1]])

    for data in cut_array:
        data.sort()

    for i in range(len(cut_array)):
        answer.append(cut_array[i][commands[i][2]-1])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
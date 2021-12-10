from collections import Counter

def solution(participant, completion):
    comp_dict = Counter()
    for p in participant:
        comp_dict[p] += 1
    for c in completion:
        comp_dict[c] -= 1

    answer = ''
    for k, v in comp_dict.items():
        if v != 0:
            answer += k

    return answer
    # return list((Counter(participant) - Counter(completion)).keys())[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

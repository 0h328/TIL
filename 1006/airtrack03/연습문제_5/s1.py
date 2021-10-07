"""
연습문제 5. 순열

5-1) 단순하게 순열 생성하기
[1, 2, 3]을 포함하는 모든 순열을 반복문을 활용하여 구현하시오.
"""

nums = [1, 2, 3]

for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j:
            for k in range(len(nums)):
                if i != k and j != k:
                    print(nums[i], nums[j], nums[k])

"""
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""
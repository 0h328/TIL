"""
연습문제 4. 순열

4-1) 단순하게 순열 생성하기
[1, 2, 3]을 포함하는 모든 순열을 반복문을 활용하여 구현하시오.
"""

nums = [1, 2, 3]

for i in nums:
    for j in nums:
        if i != j:
            for k in nums:
                if i != k and j != k:
                    print(i, j, k)
"""
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""
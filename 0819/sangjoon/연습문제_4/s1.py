## 연습문제 4 (결과 확인)

# > 재귀 함수 호출시에 Stack Frame이 어떻게 형성되는지 관찰!!
# > 파이썬 튜터보단 디버거를 충분히 활용하도록 연습해주세요. 😄
# 디버거를 통해 결과를 확인해보세요
# print 결과는 디버거를 실행 시켰을 때 보이는 'Console'이라는 탭에서 확인 가능합니다.


def func2():
    print("함수 2 시작")
    print("함수 2 종료")


def func1():
    print("함수 1 시작")
    func2()
    print("함수 1 종료")


print("메인시작")
func1()
print("메인끝")

"""
메인시작
함수 1 시작
함수 2 시작
함수 2 종료
함수 1 종료
메인끝
"""

# global 영역부터 각 함수의 고유한 영역을 디버거에서 확인해보세요!

n = 10


def f1(a):
    f2(a)


def f2(b):
    f3(b)


def f3(c):
    print(c ** 2)


f1(n)  # 100

# 반드시 디버거를 통해 결과를 확인해주세요!


def factorial(n):
    if n == 1:  # base case -> 종료 조건
        return 1
    return n * factorial(n - 1)  # 인자의 크기가 1씩 줄어감


print(factorial(5))

"""
Step 1. 
|  2 * factorial(1)  |
|  3 * factorial(2)  |
|  4 * factorial(3)  |
|  5 * factorial(4)  |
|  main  |

Step2.
2-1.
|  2 * 1  |
|  3 * factorial(2)  |
|  4 * factorial(3)  |
|  5 * factorial(4)  |
|  main  |

2-2.
|    |
|  3 * 2  |
|  4 * factorial(3)  |
|  5 * factorial(4)  |
|  main  |

2-3.
|    |
|    |
|  4 * 6 |
|  5 * factorial(4)  |
|  main  |

2-4.
|    |
|    |
|    |
|  5 * 24  |
|  main  |

2-5. 
|    |
|    |
|    |
|  120 반환 |
|  main  |

2-6. 끝
|    |
|    |
|    |
|    |
|    |
"""


# 재귀로 배열의 각 요소 출력
# 반드시 디버거를 활용하여 결과를 확인해주세요!!

a = [1, 2, 3]
N = len(a)


def f(i, N, a):
    if i == N:
        return  # return None
    # else:
    print(a[i])
    f(i + 1, N, a)
    # return이 없으면? None을 return


f(0, N, a)

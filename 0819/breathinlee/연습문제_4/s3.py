# 반드시 디버거를 통해 결과를 확인해주세요!

def factorial(n):
    if n == 1:                # base case -> 종료 조건
        return 1
    return n * factorial(n-1) # 인자의 크기가 1씩 줄어감

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
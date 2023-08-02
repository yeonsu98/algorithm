# Dynamin Programming : 다이나믹 프로그래밍
# - 중복이 발생하는 연산을 줄이자
# - 최적의 해를 구하기 위해서 시간이나 메모리가 너무 많이 필요하면 컴퓨터도 풀기가 벅차다

# - DP 적용 대상
# 1. 큰 문제를 작은 문제로 나눌 수 있어야 한다.
# - 재귀 함수 이용 (Top-Down)

# 2. 작은 문제에서 구한 해는 큰 문제에서도 동일하게 적용된다.
# - 반복을 이용 (Bottom-Up)

# 점화식(재귀식) : 수열에서 이웃하는 두 개의 항 사이에 성립하는 관계를 나타냄

# 1. 피보나치 수열 -> No DP
def fibo(n):
    if n <= 2:
        return 1
    
    return fibo(n-1) + fibo(n-2)

def bpFibo(n):
    # Dp-Table
    # - 작은(=앞) 문제를 처리하고 저장한 테이블
    # - 이 테이블은 큰(=뒤) 문제에 활용될 수 있음
    result = [0] * (n+1)
    result[1] = 1
    result[2] = 1
    
    for i in range(3, n+1):
        result[i] = result[i-1] + result[i-2]

    #print(result)

    return result[-1]
result = bpFibo(100)

result = [0] * 10
def tdFibo(n):
    if n <= 2:
        return 1
    
    # 2. 이전에 구한 적이 있는 값이면 그 값을 바로 반환
    if result[n] != 0:
        return result[n]
    
    # 1. 구한 적이 없는 값이면 재귀로 구해온다. 그 후 저장
    result[n] = tdFibo(n-1) + tdFibo(n-2)

    return result[n]
result = tdFibo(6)
print(result)
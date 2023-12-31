# 피보나치 수열
# 앞의 두 항의 값이 새로운 항이 되는 수열
# 1. 1번째와 2번째는 1로 시작한다
# 2. n번째는 (n-1)과 (n-2)번째의 합이다
# 3. 점화식은 f(n) = f(n-1) + f(n-2)
# 단, f(1) = f(2) = 1
# ex) 1 1 2 3 5 8 13 21 34 ...

def fibo(n):

    if n > 0 and n <= 2:
        return 1
    return fibo(n-1) + fibo(n-2)
    
n = fibo(6)
print("n =", n)

print("9번째 :", fibo(9))

for i in range(1, 41):
    print(f"{i}번째 fibo = {fibo(i)}")
# 숫자가 커질수록 시간이 오래 걸림
# 왜 그럴까? 재귀식의 깊이가 깊어질 수록 중복연산이 많이 발생하게 됨
# 예) f(5) - f(4) - f(3)
#         - f(3) - f(2)
#         - f(2) - f(1)
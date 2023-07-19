# lambda
# - lamda식 간략화된 식을 의미
# - 프로그래밍에서는 보통 익명함수 의미

def adder(n1, n2):
    return n1 + n2

n = lambda x, y : x + y

print("adder =", adder(5, 3))
print("n =", n)             # n은 변수, 람다식을 저장하고 있음
print("n(6, 1) =", n(6, 1)) # 변수에 함수 호출처럼 값을 전달하면 람다식이 수행


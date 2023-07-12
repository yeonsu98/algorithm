# 재귀 : 다시 되돌아오다
# 코드에 재귀는 보통 함수로 구현된다
# 이를 '재귀 함수'라고 한다
# 재귀 함수는 보통 함수에서 자기 자신을 호출해서 구현


# 1. 반복은 편도
for i in range(3, 0, -1) :
    print(i, end = " ")
print()


# 2. 재귀는 왕복
def func(n) :
    if n == 0 :         # 재귀는 종료가 되지 않으면
        return          # 무한 루프에 빠진다

    print(n, end = " ") # 재귀 전

    func(n - 1)         # 재귀 발생

    print(n, end = " ") # 재귀 후

func(3)
# 최대/최소값 : 데이터 중 가장 큰 값과 작은 값을 찾는 알고리즘

q = "세 정수 입력 : "
n1, n2, n3 = map(int, input(q).split())

print(f"n1 = {n1}, n2 = {n2}, n3 = {n3}")

mx = n1

if mx < n2 :    # 현재 최대(mx)보다 큰 값이야?
    mx = n2     # 이제 니가 최대 값이다~~
if mx < n3 :
    mx = n3

print("최대값 :", mx)


# ※ Python에는 max(), min() 함수가 기본 제공된다
mn = min(n1, n2, n3)
print("최소값 :", mn)
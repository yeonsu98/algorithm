# 현재 건물에는 엘리베이터 2대가 있다
# 건물은 1 ~ 15층까지 있고
# A는 5층에, B는 7층에 있다
# 사용자에게 현재 층 수를 입력 받아서 가까운 엘리베이터를 호출
# 만약, 층 수가 같으면 A를 호출한다

A, B = 5, 7
cur = int(input("현재 층 수? "))

disA = abs(cur - A)
disB = abs(cur - B)

# print(f"A = {disA}, B = {disB}")

if disA <= disB :
    print("A를 호출 합니다")
else :
    print("B를 호출 합니다")
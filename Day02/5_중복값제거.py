# 중복값 : 동일한 데이터
# 중복의 단점 : 용량 높임, 성능 낮춤, 무결성 낮춤

import random as r

# 함수로 짜기
def inData(result, n):
    for m in result:        # 1. 결과 리스트 값을 꺼낸다
        if n == m:          # 2. 전달 받은 값과 1번 값을 비교한다
            return False    # 3. 같으면 있는 데이터이므로 거짓을 반환
    return True             # 4. 반복 끝날 때까지 거짓이 반환되지 않음 -> 없는 데이터
        

li = [r.randint(1, 3) for i in range(10)]
print("li =", li)

# 여기에 코드를 작성해서 동일한 데이터는 1개만 출력되도록

# set 함수 이용하여
# li = list(set(li))
# print("li =", li)

result = []

for n in li:
    #if n not in result:
    if inData(result, n):
        result.append(n)

print("result =", result)

# 언어 공부할 때 도움되는 사이트 => 실행과정을 시각화해서 볼 수 있음
# https://pythontutor.com/

# 참조 변수에서 복사는 가리키는 방향이 복사됨
# 예) result = [] empty list
# inData(result, n) => result -> empty list
# 중복값 : 동일한 데이터
# - 중복의 단점 : 용량↑, 성능↓, 무결성↓

import random as r

def inData(result, n) :
    for m in result :       # 1. 결과 리스트의 값을 꺼낸다
        if n == m :         # 2. 전달 받은 값과 1번 값을 비교한다
            return False    # 3. 같으면 있는 데이터이므로 거짓을 반환

    return True             # 4. 반복 끝날때까지 거짓이 반환되지 않음 -> 없는 데이터

li = [r.randint(1, 3) for i in range(10)]
print("li =", li)

# 여기 코드를 작성해서 동일한 데이터는 1개만 출력되게 한다
result = []

for n in li :
    if inData(result, n) :
        result.append(n)

print("result =", result)
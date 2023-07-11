# python을 사용한다면 중복은 set 타입으로 쉽게 처리 가능
# python은 묶음 자료형들
# 1. List : 순서 ㅇ, 중복 ㅇ, 수정 ㅇ => 주로 같은 타입을 여러 개 저장 시 사용
# 2. Tuple : 순서 ㅇ, 중복 ㅇ, 수정 x => 다른 여러 타입을 묶어서 표현 시 사용
# 3. Set : 순서 x, 중복 x, 수정 x, 제거 ㅇ => 주로 중복 제거 시 사용       
# 4. Dict : key, value의 한 쌍으로 저장, 다른 여러 타입을 묶어서 표현 시 사용

import random as r
                                                                            #    (1 ~ 5) * 10
li = [r.randint(1, 5) for i in range(10)] # 10, 20, 30, 40, 50 만 나오게 r.randint(1, 5)*10
print("li =", li)

st = set(li)                # 1. List를 Set으로 형변환, 중복 제거
print("st =", st)

li = list(st)               # 2. 다시 List로 형변환, index 사용 및 정렬 등을 사용 가능 # set은 index가 없어서 list로 변환해서 사용
li.sort()                   # 오름차순 정렬
print("li =", li)           
li.sort(reverse=True)
print("li =", li)           # 내림차순 정렬
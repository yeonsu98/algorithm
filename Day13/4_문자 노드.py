# 리스트(or 튜플)은 index. 즉, 숫자로 데이터를 접근
# - 요소가 많으면 데이터를 특정하기가 힘들다
per1 = [
    "홍길동",
    30,
    176.3,
    "남성",
    "부산 광역시 해운대구"
]

print("per1 주소 :", per1[4])


# 딕셔너리는 key. 즉, 문자열로 데이터를 접근
per2 = {
    "name" : "홍길동",
    "age" : 30,
    "height" : 176.3,
    "gender" : "남성",
    "address" : "부산 광역시 해운대구"
}

print("per2 주소 :", per2["address"])
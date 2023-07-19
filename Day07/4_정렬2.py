li = [
    ("hong", 17, 168.3),
    ("kim", 16, 170.3),
    ("lee", 17, 190)
]
print("li =", li)

li.sort()   # 리스트의 첫번째 요소 기준으로 정렬
print("li =", li)

li.sort(reverse=True)
print("li =", li)

li.sort(key=lambda x : x[1])
print("li =", li)

# 만일 비교기준의 값이 동일한데 따로 지정하지 않으면 x[0] 요소로 지정
li.sort(key=lambda x : (x[1]))
print("li =", li)

# 2, 3 ... n순위 순서를 주려면 튜플로 묶어서 전달
li.sort(key=lambda x : (x[1], -x[2]))
print("li =", li)

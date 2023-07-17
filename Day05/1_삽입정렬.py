# 삽입 정렬 : 특정 데이터를 적절한 위치에 끼워넣어 정렬
# i : 1번 ~ 마지막까지
# j : 0번 ~ i전까지

li = [4,8,2,7,6]

for i in range(1, len(li)):
    for j in range(0, i):
        if li[i] < li[j]:
            n = li.pop(i)
            li.insert(j, n) # list j 위치에 n 넣기

print("li =", li)
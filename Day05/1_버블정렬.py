# 버블정렬 : 인접한 두 데이터를 비교하며 정렬하는 방식
# i : 0 ~ 마지막 전까지 

li = [4,8,2,7,6]

while True: # 무한반복으로 묶는 것을 권장
    cnt = 0
    for i in range(len(li)-1):
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i]
            cnt += 1
    if cnt == 0:
        break
        

print("li =", li)
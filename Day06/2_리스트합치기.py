# 병합 정렬을 위해선 분할 후 합칠 때 두 리스트를 정렬하며 합쳐야 한다.

def listMerge(li1, li2):

    result = []
    
    # 1. 둘 중 하나가 빈 리스트가 될 때까지 반복
    while li1 and li2:
        if li1[0] < li2[0]: # 2. 제일 앞 데이터를 비교해서 결과 리스트에 추가
            result.append(li1.pop(0))
        else:
            result.append(li2.pop(0))

    # 3. 반복 후 남은 요소를 result에 추가
    result += li1
    result += li2

    return result

li1 = [1,3,5,7,9]
li2 = [2,4,6,8,10]

print("li1 + li2 =", li1 + li2)

result = listMerge(li1, li2)
print("병합 정렬 :", result)

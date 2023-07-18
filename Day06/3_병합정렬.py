def mergeSort(li):
    if len(li) <= 1:
        return li
    
    # 1. 중간 위치(=index)를 구한다
    mid = len(li) // 2

    # 2. 재귀로 분할 시작
    left = mergeSort(li[:mid])
    right = mergeSort(li[mid:])
    
    # 3. 분할 후 합병 진행
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right

    return result

li = [21,10,12,20,25,13,15,22]
li = mergeSort(li)
print("li =", li)
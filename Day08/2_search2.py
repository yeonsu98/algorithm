# 이진탐색

def binarySearch(li, key):

    s = 0
    e = len(li)-1
    
    while s <= e:
        m = (s+e)//2

        if (key == li[m]):
            return m
        elif (key < li[m]):
            e = m - 1
        else:
            s = m + 1
        

li = [5,6,10,11,21,9,15,13]
li.sort()

print("li =", li)

index = binarySearch(li, 9)
print(index)
li1 = [5,3,7,8,1,2,4]
li2 = li1[:]
li3 = li1[:]

li1.sort()
print("li1 =", li1)

li2.sort(reverse=True)
print("li2 =", li2)

# lambda 매개변수 x에는 list가 들어간다
li3.sort(key=lambda x : -x)
print("li3 =", li3)
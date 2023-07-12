import random as r

li = [r.randint(1, 100) for i in range(10)]

print("li =", li)

mx = li[0]

for n in li :
    if mx < n :
        mx = n

print("최대값 :", mx)

mn = min(li)
print("최소값 :", mn)
# 3_Quiz.py 문제에서
# 엘리베이터를 3대로 변경해서 풀어보세요
# A, B, C는 랜덤으로 배치

import random as r

A = r.randint(1, 15)
B = r.randint(1, 15)
C = r.randint(1, 15)

print(f"A = {A}, B = {B}, C = {C}")
cur = int(input("현재 층 수? "))

disA = abs(cur - A)
disB = abs(cur - B)
disC = abs(cur - C)

result = ('A', disA)

if result[1] > disB :  
    result = ('B', disB)
if result[1] > disC :  
    result = ('C', disC)

print(f"{result[0]}엘리베이터를 호출")


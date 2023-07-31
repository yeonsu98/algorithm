# https://www.acmicpc.net/problem/18406
# 쉬는시간~

n = input()

mid = len(n) // 2
left = n[:mid]
right = n[mid:]

result = 0

for i in left:
    result += int(i)

for i in right:
    result -= int(i)

if result == 0  : print("LUCKY")
else            : print("READY")
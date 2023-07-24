# Implements : 구현
# - 생각해낸 알고리즘을 코드로 구현하는 것
# - 생소한 개념이나 코드에 대한 이해도가 부족할 수 있음

# ex01.png
n = int(input())
cmd = input().upper().split()

# 시작은 항상 (1, 1)
x ,y = 1, 1 

#     상   하   좌   우
dx = [-1,  1,  0,  0]
dy = [0,  0,  -1,  1]

mv = ['U','D','L','R']

for c in cmd:
    for i in range(len(mv)):
        if c == mv[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    # 맵을 벗어났을 때
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    # 검증 후 실제 x, y에 적용
    x, y = nx, ny
    # debugging
    # print(f"디버깅({c}) : {x, y}") # 공간 밖으로 나가는 것을 처리해주지 않음

print(x, y)

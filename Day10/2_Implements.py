# ex02.py

cmd = input()
x = int(cmd[1])
y = ord(cmd[0])-96

mv = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

cnt = 0     # 가능한 경우의 수

for m in mv:

    # 점검을 위한 nx, ny 변수 만들기
    nx = x + m[0]
    ny = y + m[1]

    # 범위를 벗어나는 지 확인
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue    # 벗어난다면 가능한 경우의 수에 포함하지 않기

    # 범위를 벗어나지 않는다면 가능한 경우의 수에 추가
    cnt += 1
    
print(cnt)